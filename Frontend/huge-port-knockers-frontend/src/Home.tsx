import { useNavigate } from "react-router-dom";
import { KnockerTable } from "./components/KnockerTable";
import { Button } from "@mui/material";


export const Home: React.FC = () => {
    
    const navigate = useNavigate();

    const handleClick = () => {
        navigate('/about');
    }

    return (
        <>
            <h1>Port Knockers</h1>
            <KnockerTable/>
            <Button sx={{marginTop: 10, fontSize: 20}} onClick={handleClick}>About this Project</Button>
        </>
    )
    }

export default Home;

