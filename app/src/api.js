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
  getBoards() {
    return this.execute('get', `boards/`)
  },
  getBoard(id) {
    return this.execute('get', `boards/${id}/`)
  },
  getLanes() {
    return this.execute('get', 'lanes/')
  },
  getCards() {
    return this.execute('get', 'cards/')
  }
}
