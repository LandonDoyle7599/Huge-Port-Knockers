# Port-Knockers
This project uses eBPF to implement a demonstration of port knocking authentication.

## Instructions to run:
### Frontend:
with latest nodejs, npm, react, and vite packages \
npm run dev -- --host

### Backend:
If it is your first time running the backend \
cp .env.example .env \
Modify the .env file to have the ip of the system hosting the backend \
sudo apt install python3-flask \
sudo apt install python3-flask-cors \
sudo ./backend.py 

### Port forwarding from VM
Add two port forwarding rules \
Host IP: 127.0.0.1, Host Port: 5000, Guest Port: 5000 \
Host IP: 127.0.0.1, Host Port: 5173, Guest Port: 5173 

### Created by:
Landon Doyle \
Bryce Collins \
Erik Johnson \
Nicholas Hedges
