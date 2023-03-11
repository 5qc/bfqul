function popup(content) {
    document.body.innerHTML += `<div class="screen" onclick="this.remove();document.querySelector('.popup').remove()"></div><div class="popup">${content}</div>`;
}
//# sourceMappingURL=script.js.map