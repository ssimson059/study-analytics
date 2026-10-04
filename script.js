const form=document.getElementById("chatForm");
const input=document.getElementById("message");
const chat=document.getElementById("chat");

function addMessage(text,type){
  const div=document.createElement("div");
  div.className="msg "+type;
  div.textContent=text;
  chat.appendChild(div);
  chat.scrollTop=chat.scrollHeight;
}

form.addEventListener("submit",async(e)=>{
  e.preventDefault();
  const message=input.value.trim();
  if(!message)return;
  addMessage(message,"user");
  input.value="";
  const loading=document.createElement("div");
  loading.className="msg bot";
  loading.textContent="Thinking...";
  chat.appendChild(loading);
  chat.scrollTop=chat.scrollHeight;

  try{
    const response=await fetch("/chat",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({message})
    });
    const data=await response.json();
    loading.remove();
    addMessage(data.reply || data.error || "Sorry, something went wrong.","bot");
  }catch(error){
    loading.remove();
    addMessage("Unable to connect to the server. Please try again.","bot");
  }
});
