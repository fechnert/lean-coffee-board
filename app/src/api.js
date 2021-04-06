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
  getBoard(board_id) {
    return this.execute('get', `boards/${board_id}/`)
  },
  getLanesOfBoard(board_id) {
    return this.execute('get', `lanes/?board=${board_id}`)
  },
  getCardsOfLane(lane_id) {
    return this.execute('get', `cards/?lane=${lane_id}`)
  }
}
