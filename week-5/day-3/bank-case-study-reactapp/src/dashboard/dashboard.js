import React from 'react';
import {
    Outlet
} from "react-router-dom";

export function Dashboard() {

    const toady = () => {

        const newDate = new Date()
        const date = newDate.getDate();
        const month = newDate.getMonth() + 1;
        const year = newDate.getFullYear();

        return `Today : ${year}-${month < 10 ? `0${month}` : `${month}`}-${date}`
    }

    return (
        <div className="container">
            <div className="mt-3 alert alert-info d-flex justify-content-between" role="alert">
                <label>Welcome {'abc'}</label>
                <label>{toady()}</label>
            </div>
            <div className="row">
                <Outlet />
            </div>
        </div >
    )
}



