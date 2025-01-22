import subprocess

def run_postman_collection():
    command = [
        "newman",
        "run",
        "postman.json",
        "--reporters", "cli,junit",
        "--reporter-junit-export", "reports/report.xml"
    ]
    subprocess.run(command, check=True)

if __name__ == "__main__":
    run_postman_collection()
    print("Postman collection tests completed.")
