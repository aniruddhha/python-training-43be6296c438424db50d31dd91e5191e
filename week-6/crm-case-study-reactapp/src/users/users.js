import { apiListCrmUsers } from './crm-user-list-rest-api'
import { useEffect, useState } from 'react'
import './users.css'
import { Modal } from 'react-bootstrap'

export function CrmUser() {

    const [users, setUsers] = useState([])
    const [modalShow, setModalShow] = useState(false)
    const [modalTitle, setModalTitle] = useState()
    const [modalBody, setModalBody] = useState()

    useEffect(() => { // used for calling rest api at the time of initial render
        apiListCrmUsers().then(json => {
            const urs = json['res']

            setUsers(urs)
        })
    }, [])

    const onOperationClicked = op => {
        setModalShow(true)
        setModalTitle(op['status'] ? 'Deactivating User' : 'Activating User')
        setModalBody(`${op['mobile']}`)
    }

    const onModalHide = () => {
        setModalShow(false)
    }

    const trUsers = users.map((usr, inx) => {
        return (
            <tr key={inx}>
                <td>{inx + 1}</td>
                <td>{usr['mobile']}</td>
                <td>{usr['role']}</td>
                <td>{usr['doj']}</td>
                <td>{usr['status'] ? '✅' : '❌'}</td>
                <td>
                    <u onClick={() => onOperationClicked(usr)}>{usr['status'] ? 'deactivate' : 'activate'}</u>
                </td>
            </tr>
        )
    })

    return (
        <>

            <div className='container border border-primary'>
                <div className='row'>
                    <div className='column'>
                        <h3 className='text-muted'> Crm Users </h3>
                    </div>
                </div>
                <div className='row'>
                    <table className="table">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Mobile</th>
                                <th scope="col">Role</th>
                                <th scope="col">Joining</th>
                                <th scope="col">Status</th>
                                <th scope="col">Operation</th>
                            </tr>
                        </thead>
                        <tbody>
                            {trUsers}
                        </tbody>
                    </table>
                </div>
            </div>

            <Modal show={modalShow} onHide={onModalHide}>
                <Modal.Header closeButton>
                    <Modal.Title>{modalTitle}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    {modalBody}
                </Modal.Body>
                <Modal.Footer>
                    <input
                        type='button'
                        className='btn btn-outline-secondary'
                        value="Cancel"
                        onClick={onModalHide}
                    />

                    <input
                        type='button'
                        className='btn btn-primary'
                        value="Okay"
                    />
                </Modal.Footer>
            </Modal>
        </>
    )
}