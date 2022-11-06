import React from "react";

const Footer = () => {
    let year = new Date();

    return (
        <footer>
            <div className="mt-auto text-center bg-dark text-light py-2">
                <h6>Recipe Suggestion &copy; - {year.getFullYear()}</h6>
                <h6>Created by Jun Lin, Kai Lin, and Muhaimin Sarker</h6>
            </div>
        </footer>
    );
};

export default Footer;