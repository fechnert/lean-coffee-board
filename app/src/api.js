// import Vue from 'vue'
import axios from 'axios'

const client = axios.create({
  baseURL: 'http://localhost:8000/api/',
  json: true
})

export default {
  async execute(method, resource, data) {
    // inject the accessToken for each request
    //let accessToken = await Vue.prototype.$auth.getAccessToken()
    let accessToken = "";
    return client({
      method,
      url: resource,
      data,
      headers: {
        Authorization: `Token ${accessToken}`
      }
    }).then(req => {
      return req.data
    })
  },
  getBoard(boardId) {
    return this.execute('get', `boards/${boardId}/`)
  },
  getLanesOfBoard(boardId) {
    return this.execute('get', `lanes/?board=${boardId}`)
  },
  getCardsOfLane(laneId) {
    return this.execute('get', `cards/?lane=${laneId}`)
  },
  createCard(ownerId, boardId, LaneId, title) {
    return this.execute('post', `cards/`, {
      owner: ownerId,
      board: boardId,
      lane: LaneId,
      title: title,
    })
  },
  deleteCard(cardId) {
    return this.execute('delete', `cards/${cardId}/`)
  },
}
