import { useEffect, useState } from 'react';
import { Knocker } from '../models';
import { CircularProgress } from '@mui/material';


export const KnockerTable = () => {

    const [data, setData] = useState<Knocker[]>([]);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const interval = setInterval(() => {
            fetch('http://localhost:5000/data')
                .then(response => response.json())
                .then(data => {
                setData(data);
                setLoading(false);
          });
        }, 500);
        return () => clearInterval(interval);
    }, []);

    const headers = ['IP Address', 'Ports Knocked', 'Authenticated'];

    const allPortsCorrect = (ip: string) => {
        const knocker = data.find(knocker => knocker.ip === ip);
        if (!knocker) return false;
        return knocker.ports.every(port => port.correct);
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
                    {data.map((knocker, index) => {
                        return (
                            <tr key={index}>
                                <td style={{fontSize:30, borderRight: "2px solid white", borderBottom: '2px solid white'}}>{knocker.ip}</td>
                                <td style={{borderRight: "2px solid white", borderBottom: '2px solid white'}}>
                                    <ul>
                                        {knocker.ports.map((port, index) => {
                                            return (
                                                <td key={index} style={{ fontSize: 30, backgroundColor: port.correct ? 'green' : 'red' }}>
                                                    {port.port}
                                                </td>
                                            )
                                        })}
                                        {knocker.ports.length < 4 && allPortsCorrect(knocker.ip) && 
                                        <td>
                                            <CircularProgress/> 
                                        </td>}
                                    </ul>
                                </td>
                                {knocker.ports.length === 4 && allPortsCorrect(knocker.ip) && <td style={{ borderBottom: '2px solid white', borderRight: '2px solid white', backgroundColor: 'Green', fontSize:30 }}>Authenticated</td>}
                                {knocker.ports.length < 4 && allPortsCorrect(knocker.ip) && <td style={{ borderBottom: '2px solid white', borderRight: '2px solid white', backgroundColor: 'blue', fontSize:30}}>Authenticating</td>}
                                {!allPortsCorrect(knocker.ip) && <td style={{ backgroundColor: 'red', borderRight: '2px solid white', borderBottom: '2px solid white', fontSize:30}}>Authentication Failed</td>}
                            </tr>
                        )
                    })}
                </tbody>
            </table>
}
        </div>
    )

}