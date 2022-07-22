const express = require('express')
const app = express()
const port = 3001
const mysql = require('mysql2')
const cors = require('cors')

let connection = mysql.createPool({
  host     : 'localhost',
  port     : '3306',
  user     : 'root',
  password : '',
  database : 'meucrud'
})
 
app.use(cors())
app.use(express.json())

app.delete("/delete/:id",(req,res)=>{
  const {id} = req.params

  let SQL = "DELETE FROM games WHERE idgames= ?"

  connection.query(SQL,[id],(err,result)=>{
    if (err) console.log(err)
    else res.send(result)
})
})

app.put("/edit",(req,res)=>{
  const {id} = req.body
  const {name} = req.body
  const {cost} = req.body
  const {category} = req.body

  let SQL = "UPDATE games SET name = ?, cost = ?, category = ? WHERE idgames = ?"

  connection.query(SQL,[name,cost,category,id],(err,result)=>{
    if (err) console.log(err)
    else res.send(result)
})
})

app.post("/register",(req,res)=>{
  const {name} = req.body
  const {cost} = req.body
  const {category} = req.body 

  let SQL = 'INSERT INTO games (name,cost,category) VALUES (?,?,?)'

  connection.query(SQL,[name,cost,category],(err,result)=>{
    console.log(err)
    /*if (err) console.log(err)
    else res.send(result)*/
  })
})

app.get("/getCards",(req,res)=>{

  let SQL = 'SELECT * FROM games'

  connection.query(SQL,(err,result)=>{
    if (err) console.log(err)
    else res.send(result)
  })
})




app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})