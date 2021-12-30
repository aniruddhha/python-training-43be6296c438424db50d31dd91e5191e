import { apiListCrmUsers, apiActivateDeactivateUser } from './crm-user-list-rest-api'
import { useEffect, useState, useCallback } from 'react'
import './users.css'
import { Modal } from 'react-bootstrap'

export function CrmUser() {

    const [users, setUsers] = useState([])
    const [modalShow, setModalShow] = useState(false)
    const [modalTitle, setModalTitle] = useState()
    const [modalBody, setModalBody] = useState()
    const [clickedUser, setClickedUser] = useState({})

    useEffect(() => { // used for calling rest api at the time of initial render
        apiListCrmUsers().then(json => {
            const urs = json['res']
            setUsers(urs)
        })
    }, [])

    const onOperationClicked = usr => {
        setModalShow(true)
        setModalTitle(usr['status'] ? 'Deactivating User' : 'Activating User')
        setModalBody(`${usr['mobile']}`)
        setClickedUser(usr)
        console.log(usr)
    }

    const onModalHide = () => setModalShow(false)

    const onOkayClicked = () => makePutActivateDeactivateRequest()

    const makePutActivateDeactivateRequest = useCallback(() => {
        console.log(clickedUser)
        const admin_id = localStorage.getItem('mobile')
        const user_id = clickedUser['mobile']
        const sts = clickedUser['status'] == 0 ? 1 : 0

        apiActivateDeactivateUser(admin_id, user_id, sts).then(res => {
            if (res['sts'] == 'success') {
                setModalShow(false)
            }
        })
    }, [clickedUser, modalShow])

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
                        onClick={onOkayClicked}
                    />
                </Modal.Footer>
            </Modal>
        </>
    )
}