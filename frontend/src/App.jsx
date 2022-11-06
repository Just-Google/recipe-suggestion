import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Nav from "./components/Nav"

function App() {
    return (
        <Router>
            <Nav></Nav>
            <Routes>
                <Route path="/" element={<Home />} />
            </Routes>
            
        </Router>
    );
}

export default App;