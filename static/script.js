async function summarize(){

let text = document.getElementById("text").value
let mode = document.getElementById("mode").value
let file = document.getElementById("fileInput").files[0]

let formData = new FormData()

formData.append("text", text)
formData.append("mode", mode)

if(file){
formData.append("file", file)
}

let response = await fetch("/summarize",{
method:"POST",
body:formData
})

let data = await response.json()

document.getElementById("summary").innerHTML = data.summary

let list = document.getElementById("keypoints")
list.innerHTML=""

data.keypoints.forEach(k=>{
let li=document.createElement("li")
li.innerText=k
list.appendChild(li)
})

}