import { useEffect, useState } from 'react';
import { Knocker } from '../models';

const mockData: Knocker[] = [
    {
        ip: "192.168.1.2",
        ports: [
            {
                port: 22,
                correct: true
            },
            {
                port: 80,
                correct: false
            }
        ],
        authenticated: false
    },
    {
        ip: "172.1.2.1",
        ports: [
            {
                port: 22,
                correct: true
            },
            {
                port: 80,
                correct: true
            },
            {
                port: 443,
                correct: true
            },
            {
                port: 8080,
                correct: true
            }
        ],
        authenticated: true
    }
]


export const KnockerTable = () => {

    // const [data, setData] = useState<Knocker[]>([]);
    const [data, setData] = useState<Knocker[]>(mockData);
    useEffect(() => {
        const interval = setInterval(() => {
            fetch('http://localhost:5000/api')
                .then(response => response.json())
                .then(data => {
                setData(data);
          });
        }, 2000);
        return () => clearInterval(interval);
    }, []);

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
                                    <td style={{ backgroundColor: knocker.authenticated ? 'Green' : 'Red' }}>Authenticated</td>
                                    <></>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )

}