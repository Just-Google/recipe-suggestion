import React from "react";

const Ingredient = () => {

    return (
        <form style = {{textAlign:"center", padding:25}}>
            <input style = {{height: 50, width: 500}} type="text" placeholder = "Write ingredients"></input>
            <input type="submit" value="Submit"></input>
        </form>
    );
};

export default Ingredient;