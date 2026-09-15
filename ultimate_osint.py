import os
import sys
import requests
import dns.resolver
from PIL import Image
import exifread
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    console.print(Panel.fit(
        "[bold cyan]ULTIMATE ALL-IN-ONE OSINT FRAMEWORK[/bold cyan]\n"
        "[italic green]Cross-Platform: Windows | Linux | Kali | Parrot | Termux[/italic green]",
        title="[bold red]EZ-Intelligence v2.0[/bold red]",
        border_style="magenta"
    ))

# -------------------------------------------------------------
# 1. PHONE & USERNAME RECON
# -------------------------------------------------------------
def phone_lookup():
    show_banner()
    number = Prompt.ask("[bold yellow]Enter Phone Number with country code (e.g., +1234567890)[/bold yellow]")
    console.print(f"\n[cyan][*] Analyzing Phone Number structure: {number}[/cyan]\n")
    
    try:
        # Free carrier/country API lookup
        res = requests.get(f"https://api.veriphone.io/v2/verify?phone={number}&key=guest").json()
        
        table = Table(title="Phone Number Intelligence")
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="magenta")
        
        table.add_row("Valid Number", str(res.get("phone_valid", "Unknown")))
        table.add_row("Country", res.get("country", "N/A"))
        table.add_row("Carrier / Network", res.get("carrier", "N/A"))
        table.add_row("Line Type", res.get("line_type", "N/A"))
        
        console.print(table)
    except Exception:
        console.print("[red][!] Phone lookup API limit reached or invalid input.[/red]")
    
    Prompt.ask("\n[dim]Press Enter to go back...[/dim]")

def username_lookup():
    show_banner()
    username = Prompt.ask("[bold yellow]Enter Target Username[/bold yellow]")
    
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter/X": f"https://x.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Telegram": f"https://t.me/{username}"
    }

    table = Table(title=f"Username Tracker: {username}")
    table.add_column("Platform", style="cyan")
    table.add_column("URL", style="blue")
    table.add_column("Status", style="bold green")

    for site, url in platforms.items():
        try:
            res = requests.get(url, timeout=4)
            if res.status_code == 200:
                table.add_row(site, url, "EXISTS")
            else:
                table.add_row(site, url, "[red]NOT FOUND[/red]")
        except Exception:
            table.add_row(site, url, "[yellow]TIMEOUT/ERROR[/yellow]")

    console.print(table)
    Prompt.ask("\n[dim]Press Enter to go back...[/dim]")

def digital_identity_menu():
    while True:
        show_banner()
        console.print("[bold yellow]--- Digital Identity & People Search ---[/bold yellow]\n")
        console.print("1. Phone Number Information Lookup")
        console.print("2. Username Finder Across Platforms")
        console.print("3. Back to Main Menu\n")
        
        c = Prompt.ask("Select an option", choices=["1", "2", "3"])
        if c == "1": phone_lookup()
        elif c == "2": username_lookup()
        elif c == "3": break

# -------------------------------------------------------------
# 2. NETWORK & INFRASTRUCTURE RECON
# -------------------------------------------------------------
def network_recon():
    show_banner()
    target = Prompt.ask("[bold yellow]Enter Domain or IP Address (e.g., target.com)[/bold yellow]")
    
    table = Table(title=f"Network Reconnaissance: {target}")
    table.add_column("Field", style="cyan")
    table.add_column("Details", style="magenta")

    # IP Geolocation
    try:
        ip_res = requests.get(f"https://ipapi.co/{target}/json/").json()
        table.add_row("Resolved IP", ip_res.get("ip", "N/A"))
        table.add_row("Country / City", f"{ip_res.get('country_name', 'N/A')} - {ip_res.get('city', 'N/A')}")
        table.add_row("ASN / ISP", f"{ip_res.get('asn', 'N/A')} / {ip_res.get('org', 'N/A')}")
    except Exception:
        table.add_row("Geolocation", "Failed to resolve")

    # DNS MX/NS Records
    try:
        answers = dns.resolver.resolve(target, 'MX')
        mx_records = ", ".join([str(r.exchange) for r in answers])
        table.add_row("MX Records", mx_records)
    except Exception:
        table.add_row("MX Records", "None/Failed")

    console.print(table)
    Prompt.ask("\n[dim]Press Enter to go back...[/dim]")

# -------------------------------------------------------------
# 3. IMAGERY & GEOSPATIAL INTELLIGENCE
# -------------------------------------------------------------
def image_geospatial():
    show_banner()
    console.print("[bold yellow]EXIF Metadata & Geospatial Extractor[/bold yellow]\n")
    img_path = Prompt.ask("Enter full path to Image file (e.g., photo.jpg)")

    if not os.path.exists(img_path):
        console.print("[red][!] File does not exist on this path.[/red]")
    else:
        try:
            with open(img_path, 'rb') as f:
                tags = exifread.process_file(f)
                
            table = Table(title="Extracted EXIF / Metadata")
            table.add_column("EXIF Tag", style="cyan")
            table.add_column("Value", style="magenta")
            
            found = False
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    table.add_row(str(tag), str(tags[tag])[:50])
                    found = True
            
            if found:
                console.print(table)
            else:
                console.print("[yellow][!] No EXIF metadata or GPS header found in image.[/yellow]")
        except Exception as e:
            console.print(f"[red][!] Image read error: {e}[/red]")
            
    Prompt.ask("\n[dim]Press Enter to go back...[/dim]")

# -------------------------------------------------------------
# 4. LEAKED DATA & SOURCE CODE RECON
# -------------------------------------------------------------
def leaked_data_recon():
    show_banner()
    email = Prompt.ask("[bold yellow]Enter Email Address to Check Public Leaks[/bold yellow]")
    
    console.print(f"\n[cyan][*] Searching public breach databases for {email}...[/cyan]\n")

    try:
        url = f"https://api.xposedornot.com/v1/check-email/{email}"
        res = requests.get(url, timeout=5)
        
        if res.status_code == 200 and "Exposed" in res.text:
            data = res.json()
            breaches = data.get("ExposedBreaches", {}).get("breaches", [])
            
            table = Table(title="[bold red]Public Database Leaks Detected[/bold red]")
            table.add_column("Breached Service Name", style="bold red")
            
            for b in breaches:
                table.add_row(b.get("BreachName", "Unknown Leak"))
            console.print(table)
        else:
            console.print("[bold green][+] No public breaches found for this email address.[/bold green]")
    except Exception:
        console.print("[red][!] Error querying breach search database.[/red]")

    Prompt.ask("\n[dim]Press Enter to go back...[/dim]")

# -------------------------------------------------------------
# MAIN INTERFACE CONTROL
# -------------------------------------------------------------
def main():
    while True:
        show_banner()
        console.print("1. [cyan]Digital Identity & People Search (Phone/Username)[/cyan]")
        console.print("2. [cyan]Network & Infrastructure Reconnaissance (IP/Domain/DNS)[/cyan]")
        console.print("3. [cyan]Imagery & Geospatial Intelligence (EXIF Metadata Extraction)[/cyan]")
        console.print("4. [cyan]Source Code & Leaked Data Detection (Breach Scanner)[/cyan]")
        console.print("5. [red]Exit Framework[/red]\n")
        
        choice = Prompt.ask("Choose Main Option", choices=["1", "2", "3", "4", "5"])
        
        if choice == "1":
            digital_identity_menu()
        elif choice == "2":
            network_recon()
        elif choice == "3":
            image_geospatial()
        elif choice == "4":
            leaked_data_recon()
        elif choice == "5":
            console.print("[bold green]Exiting Ultimate OSINT Framework...[/bold green]")
            sys.exit(0)

if __name__ == "__main__":
    main()