// import Vue from 'vue'
import axios from 'axios'

const client = axios.create({
  baseURL: 'http://localhost:8000/api/',
  json: true
})

export default {
  login(name, color) {
    return client.post(`login/`, {
      name: name,
      color: color,
    })
  },
  getBoard(boardId) {
    return client.get(`boards/${boardId}/`)
  },
  getBoardsByOwner(ownerId, limit=5) {
    return client.get(`boards/?owner=${ownerId}&limit=${limit}`)
  },
  getBoardsByMember(memberId, limit=10) {
    return client.get(`boards/?member=${memberId}&limit=${limit}`)
  },
  createBoard(owner, title, thinkTimeLimit, discussTimeLimit) {
    return client.post(`boards/`, {
      owner: owner,
      title: title,
      think_time_limit: thinkTimeLimit,
      discuss_time_limit: discussTimeLimit,
    })
  },
  createLaneForBoard(boardId, lane) {
    return client.post(`lanes/`, {
      board: boardId,
      title: lane.title,
      type: lane.type,
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
