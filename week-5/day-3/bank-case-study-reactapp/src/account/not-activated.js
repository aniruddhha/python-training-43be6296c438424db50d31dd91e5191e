import React from 'react'

export function NotActivated() {
    return (
        <div className="container">
            <div className="row">
                <div className="col">
                    <div className="alert alert-danger" role="alert">
                        <h4 className="alert-heading">Not Activated</h4>
                        <p>Account activation is in process</p>
                        <hr />
                        <p className="mb-0"> For more details visit your main branch and submit the application for activation </p>
                    </div>
                </div>
            </div>
        </div>
    )
}


