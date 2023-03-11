function popup(content: string) {
    document.body.innerHTML += `<div class="screen" onclick="this.remove();document.querySelector('.popup').remove()"></div><div class="popup">${content}</div>`
}