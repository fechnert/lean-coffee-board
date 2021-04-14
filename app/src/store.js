import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

// Create a new store instance.
const store = createStore({
  plugins: [createPersistedState()],
  state () {
    return {
      user: null
    }
  },
  mutations: {
    login(state, user_data) {
      state.user = {
        id: user_data.id,
        name: user_data.name,
        color: user_data.color,
        token: user_data.token,
      }
    },
    logout(state) {
      state.user = null;
    }
  }
})

export default store
