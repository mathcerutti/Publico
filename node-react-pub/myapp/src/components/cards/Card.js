import React from 'react'
import './Card.css'
import FormDialog from './dialog/dialog'

export default function Card(props){

    const [open, setOpen] = React.useState(false);
    const handleClickcard = ()=> {
        setOpen(true)
    }

    return( 
            <>
                <FormDialog 
                open={open} 
                setOpen={setOpen} 
                name={props.name} 
                cost={props.cost} 
                category={props.category}
                listCard={props.listCard}
                setListCard={props.setListCard}
                id={props.id}
                    /> 
                <div className="card-container" onClick={handleClickcard}>
                    <h1 className='card-title'>{props.name}</h1>
                    <p className='card-cost'>R$ {props.cost},00</p>
                    <p className='card-category'> {props.category}</p>
                </div>
            </>
    )
}   