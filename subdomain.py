import subprocess

def enumerate_subdomains(domain):
    try:
        # Run subfinder command
        result = subprocess.run(['subfinder', '-d', domain], capture_output=True, text=True, check=True)

        # Extract subdomains from the command output
        subdomains = result.stdout.split('\n')

        # Filter out empty lines
        subdomains = [subdomain.strip() for subdomain in subdomains if subdomain.strip()]

        return subdomains

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    # Take user input for the target domain
    target_domain = input("Enter the target domain: ")

    # Check if the user provided a non-empty domain
    if not target_domain:
        print("Invalid domain. Please provide a valid domain.")
    else:
        subdomains = enumerate_subdomains(target_domain)

        if subdomains:
            print(f"Subdomains for {target_domain}:")
            for subdomain in subdomains:
                print(subdomain)
        else:
            print(f"No subdomains found for {target_domain}")
