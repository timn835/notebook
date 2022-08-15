function sayFuck(){
    console.log('fuck1.1')
}

function deleteNote(noteId) {
    console.log('fuck2')
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      console.log(_res)
      window.location.href = "/";
    });
  }