import React from "react";
import { Link } from "react-router-dom";
import "../App.css";

const Nav = () => {
    return (
        <nav className="navbar navbar-expand-lg bg-dark">
        <h2 style={{color: "white"}}>Chinese Recipe Suggestor</h2>
        <ul className="navbar-nav me-auto mb-2 mb-lg-0 col align-items-center justify-content-end">
            <li className="nav-item">
                <Link style= {{color: "white"}}className="nav-link" to="/">
                    Home
                </Link>
            </li>
            <li className="nav-item">
                <Link  style= {{color: "white"}} className="nav-link" to="/selection">
                    Select
                </Link>
            </li>
            <li className="nav-item">
                <Link style= {{color: "white"}} className="nav-link" to="/graph">
                    Graph
                </Link>
            </li>
            <li className="nav-item">
                <Link style= {{color: "white"}} className="nav-link" to="/about">
                    About
                </Link>
            </li>
        </ul>
    </nav>
    );
};

export default Nav;
