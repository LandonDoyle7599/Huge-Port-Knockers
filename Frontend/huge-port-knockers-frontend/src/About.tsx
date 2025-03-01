import { Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

export const About = () => {

    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/');
    }

    return (
        <div>
            <h1>About this Project</h1>
            <p style={{fontSize:20}}>This project uses eBPF to implement a demonstration of port knocking authentication.</p>
            <p style={{fontSize:20}}>Read more about eBPF 
                <a href="https://ebpf.io/" target="_blank" rel="noreferrer"> here
                </a>
            </p>
            <Button sx={{fontSize:20}} onClick={handleClick}>Back to Home</Button>
        </div>
    )
}

export default About;