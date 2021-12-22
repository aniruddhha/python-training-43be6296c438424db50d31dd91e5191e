import React from 'react';
import { useState } from 'react';

export function Dashboard() {

    const [role, setRole] = useState('user')

    const adminMenus = [
        { header: 'Account', title: 'Create New Account', text: 'Creating new Bank Accounts. Admin can create new accounts for newly enrolled users.' },
        { header: 'Status', title: 'Change Account Status', text: 'It is necessary to change status of newly created bank account. Default status is inactive. ' },
        { header: 'All Accounts', title: 'Existing Accounts', text: 'Admin can see all existing accounts and perform required actions' },
        { header: 'Deposit', title: 'Money Deposit', text: 'User and Admin can deposit money to their own accounts. Admin Can deposit to any account' },
        { header: 'Withdraw', title: 'Money Withdraw', text: 'User and Admin can withdraw money to their own accounts.' },
        { header: 'Balance', title: 'Balance Enquiry', text: 'User and Admin can see balance of their respectcive accounts. Admin can see balance for any account' },
        { header: 'Transfer', title: 'Transfer Money', text: 'User and Admin can transfer money to any respectcive accounts.' }
    ]

    const userMenus = [
        { header: 'Deposit', title: 'Money Deposit', text: 'User and Admin can deposit money to their own accounts. Admin Can deposit to any account' },
        { header: 'Withdraw', title: 'Money Withdraw', text: 'User and Admin can withdraw money to their own accounts.' },
        { header: 'Balance', title: 'Balance Enquiry', text: 'User and Admin can see balance of their respectcive accounts. Admin can see balance for any account' },
        { header: 'Transfer', title: 'Transfer Money', text: 'User and Admin can transfer money to any respectcive accounts.' }
    ]

    const toady = () => {

        const newDate = new Date()
        const date = newDate.getDate();
        const month = newDate.getMonth() + 1;
        const year = newDate.getFullYear();

        return `Today : ${year}-${month < 10 ? `0${month}` : `${month}`}-${date}`
    }

    const menus = () => {
        let menusType = undefined
        if (role === 'user') {
            menusType = userMenus
        }
        else {
            menusType = adminMenus
        }
        return menusType.map((menu, index) => {
            return (
                <div key={index} className="card text-white bg-secondary mb-3 ms-3" style={{ maxWidth: '18rem' }}>
                    <div className="card-header">{menu.header}</div>
                    <div className="card-body">
                        <h5 className="card-title">{menu.title}</h5>
                        <p className="card-text">{menu.text}</p>
                    </div>
                </div>
            )
        })
    }

    return (
        <div className="container">
            <div className="mt-3 alert alert-info d-flex justify-content-between" role="alert">
                <label>Welcome {'abc'}</label>
                <label>{toady()}</label>
            </div>
            <div className="row">
                {menus()}
            </div>
        </div >
    )
}



