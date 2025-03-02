# Port-Knockers
This project uses eBPF to implement a demonstration of port knocking authentication.

## Instructions to run:
### Frontend:
with latest nodejs, npm, react, and vite packages \
npm run dev -- --host

### Backend:
python3 -m venv .venv \
. .venv/bin/activate \
pip install Flask \
pip install flask_cors \
python3 api.py 

### Port forwarding from VM
Add two port forwarding rules \
Host IP: 127.0.0.1, Host Port: 5000, Guest Port: 5000 \
Host IP: 127.0.0.1, Host Port: 5173, Guest Port: 5173 

### Created by:
Landon Doyle \
Bryce Collins \
Erik Johnson \
Nicholas Hedges
