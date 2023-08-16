echo "Starting the Uvicorin for Cisco Ping"
cd src/cisco_ping
uvicorn app:app --host 0.0.0.0 --port 9000