import { useEffect, useState } from 'react';
import { Knocker } from '../models';
import { Button, CircularProgress } from '@mui/material';
import { useNavigate } from 'react-router-dom';


export const KnockerTable = () => {

    const [knockerValues, setKnockerValues] = useState<Knocker[]>([]);
    const [loading, setLoading] = useState(true);
    const backendIP = import.meta.env.VITE_BACKEND_IP

    useEffect(() => {
        const interval = setInterval(() => {
            fetch(`http://${backendIP}:5000/data`)
                .then(response => response.json())
                .then((data) => {
                    console.log(Object.values(data)); // Extracts the values from the object
                    setKnockerValues(Object.values(data));
                    setLoading(false);
                })
                .catch(error => console.error("Error fetching data:", error));
        }, 2000);
        return () => clearInterval(interval);
    }, []);
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/about');
    }
    const headers = ['IP Address', 'Ports Knocked', 'Status'];

    const firstFourPortsCorrect = (ip: string) => {
        const ports = knockerValues.find(knocker => knocker.ip === ip)?.ports;
        if (!ports) {
            return false;
        }
        return ports[0].correct && ports[1].correct && ports[2].correct && ports[3].correct;
    }

    


    return (
        <div style={{ height: 400, width: '100%' }}>
            {loading && <CircularProgress/>}
            {!loading &&
            <table style={{ width: '100%', border: '2px solid white'}}>
                <thead>
                    <tr>
                        {headers.map((header, index) => {
                            return (
                                <th style={{borderRight: "2px solid white", borderBottom: '2px solid white', fontSize: 35, paddingRight: 10}} key={index}>{header}</th>
                            )
                        })}
                    </tr>
                </thead>
                <tbody>
                    {/* avoid knockermap.values is not a function error */}
                    {knockerValues.map((knocker, index) => {
                        return (
                            <tr key={index}>
                                <td style={{fontSize:30, borderRight: "2px solid white", borderBottom: '2px solid white'}}>{knocker.ip}</td>
                                <td style={{borderRight: "2px solid white", borderBottom: '2px solid white', marginRight: 10}}>
                                    <ul>
                                        {knocker.ports.map((port, index) => {
                                            return (
                                                <td key={index} style={{ fontSize: 30, backgroundColor: port.correct ? 'green' : 'red' }}>
                                                    {port.port}
                                                </td>
                                            )
                                        })}
                                        {knocker.ports.length < 4 && firstFourPortsCorrect(knocker.ip) && 
                                        <td>
                                            <CircularProgress/> 
                                        </td>}
                                    </ul>
                                </td>
                                {!firstFourPortsCorrect(knocker.ip) && !knocker.failed && <td style={{ borderBottom: '2px solid white', borderRight: '2px solid white', backgroundColor: 'orange', fontSize:30 }}>Authenticating</td>}
                                {knocker.connected && <td style={{ borderBottom: '2px solid white', borderRight: '2px solid white', backgroundColor: 'green', fontSize:30}}>Connected</td>}
                                {knocker.failed && <td style={{ backgroundColor: 'red', borderRight: '2px solid white', borderBottom: '2px solid white', fontSize:30}}>Authentication Failed</td>}
                                {!knocker.failed && firstFourPortsCorrect(knocker.ip) && !knocker.connected && <td style={{ borderBottom: '2px solid white', borderRight: '2px solid white', backgroundColor: 'blue', fontSize:30}}>Authenticated</td>}
                            </tr>
                        )
                    })}
                </tbody>
            </table>
}
            <Button sx={{fontSize: 20}} onClick={handleClick}>About this Project</Button>
        </div>
    )

}
