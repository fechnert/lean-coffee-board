// import Vue from 'vue'
import axios from 'axios'

const client = axios.create({
  baseURL: 'http://localhost:8000/api/',
  json: true
})

export default {
  getBoard(boardId) {
    return client.get(`boards/${boardId}/`)
  },
  createBoard(owner, title, thinkTimeLimit, discussTimeLimit) {
    return client.post(`boards/`, {
      owner: owner,
      title: title,
      think_time_limit: thinkTimeLimit,
      discuss_time_limit: discussTimeLimit,
    })
  },
  getLanesOfBoard(boardId) {
    return client.get(`lanes/?board=${boardId}`)
  },
  getCardsOfLane(laneId) {
    return client.get(`cards/?lane=${laneId}`)
  },
  createCard(ownerId, boardId, LaneId, title) {
    return client.post(`cards/`, {
      owner: ownerId,
      board: boardId,
      lane: LaneId,
      title: title,
    })
  },
  updateCard(cardId, title, lane, position) {
    return client.patch(`cards/${cardId}/`, {
      title: title,
      lane: lane,
      position: position,
    })
  },
  deleteCard(cardId) {
    return client.delete(`cards/${cardId}/`)
  },
}
