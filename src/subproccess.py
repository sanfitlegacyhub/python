import subprocess

def get_disk_space():
    try:
        # Run the df -h command and capture its output
        result = subprocess.run(['df', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        # Extract and print the output
        df_output = result.stdout
        print("Disk Space Information:")
        print(df_output)

    except subprocess.CalledProcessError as e:
        # Handle the case where the command returns a non-zero exit code
        print("Error:", e.stderr)

# Call the function to get disk space information
get_disk_space()
