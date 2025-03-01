import { useEffect, useState } from 'react';
import { Knocker } from '../models';


export const KnockerTable = () => {

    const [data, setData] = useState<Knocker[]>([]);
    useEffect(() => {
        const interval = setInterval(() => {
            fetch('http://localhost:5000/data')
                .then(response => response.json())
                .then(data => {
                setData(data);
          });
        }, 2000);
        return () => clearInterval(interval);
    }, []);

    const allPortsCorrect = (ip: string) => {
        const knocker = data.find(knocker => knocker.ip === ip);
        if (!knocker) return false;
        return knocker.ports.every(port => port.correct);
    }

    return (
        <div style={{ height: 400, width: '100%' }}>
            <table style={{ width: '100%'}}>
                <thead>
                    <tr>
                        <th>IP Address</th>
                        <th>Ports Knocked</th>
                        <th>Authenticated</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((knocker, index) => {
                        return (
                            <tr key={index}>
                                <td>{knocker.ip}</td>
                                <td>
                                    <ul>
                                        {knocker.ports.map((port, index) => {
                                            return (
                                                <td key={index} style={{ backgroundColor: port.correct ? 'green' : 'red' }}>
                                                    {port.port}
                                                </td>
                                            )
                                        })}
                                    </ul>
                                </td>
                                {knocker.ports.length === 4 && allPortsCorrect(knocker.ip) && <td style={{ backgroundColor: 'Green' }}>Authenticated</td>}
                                {knocker.ports.length < 4 && allPortsCorrect(knocker.ip) && <td style={{ backgroundColor: 'blue'}}>Authenticating</td>}
                                {!allPortsCorrect(knocker.ip) && <td style={{ backgroundColor: 'red'}}>Authentication Failed</td>}
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )

}