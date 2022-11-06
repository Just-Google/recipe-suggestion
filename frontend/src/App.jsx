import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import React, { useState, useEffect } from "react";
import Home from "./components/Home";
import Nav from "./components/Nav"

function App() {
    const [data, setdata] = useState({});
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/").then((res) =>
            res.json().then((response) => {
                // Setting a data from api
                setData(response)
            })
        );
    }, []);
    return (
        <Router>
            <Nav></Nav>
            <Routes>
                <Route path="/" element={data.data.message} />
            </Routes>
            
        </Router>
    );
}

export default App;