import { ref, reactive, computed } from "vue";
import axios from "axios";
import router from "@/router/index.ts";

  /**
  * Interfaces used for type hinting each object , same types are used on the back-end 
  * so it makes the whole state manegement quiet easer.
  */

interface Portfolio {
  id: number;
  name: string;
  description: string;
  link: string;
}
interface History {
  date: string;
  description: string;
}

interface Message {
  sender: number;
  body: string;
}

export class User {
  name: string;
  lastName: string;
  email: string;
  entity: string;
  info: {
    title: "";
    about: "";
    entity: "";
    phone: "";
    facebook: "";
    history: History[];
    skills: {}[];
  };
  portfolio: boolean;
  projects: [Portfolio];
  inbox: [Message];
  profileCompleted: number;
  messageCounter: number;
  loggedIn: boolean
}

interface UsersList {
  users: [User];
}
  /**
   * User is the main objec wich is used as state 
  */

const user = ref<User>({
  name: "",
  lastName: "",
  email: "",
  entity: "",
  info: {
    title: "",
    about: "",
    entity: "",
    phone: "",
    facebook: "",
    history: [{ date: "", description: "" }],
    skills: [],
  },
  portfolio: false,
  projects: [{ id: 0, name: "", description: "", link: "" }],
  inbox: [{sender: null, body:''}],
  profileCompleted: null,
  messageCounter: null,
  loggedIn: false
});



const users = ref<UsersList>({ users: [{} as User] });
const token = ref(localStorage.getItem("user_token"));
axios.defaults.headers.common["Authorization"] = `Bearer ${token.value}`;
const loading = ref(true)


export default function UserWork() {
  const errorMessage = ref("");
  const loggedIn = ref(false);

  const currentUser = () => {
    axios
      .get("http://127.0.0.1:8000/users/user")
      .then((response) => {
        user.value = response.data;
        user.value.loggedIn = true
      })
      .catch((error) => (errorMessage.value = error.response.data.detail));

  };

  const login = (payload: any) => {
    axios
      .post("http://127.0.0.1:8000/users/login", payload)
      .then((response) => {
        localStorage.setItem("user_token", response.data.access_token);
        user.value.loggedIn = true
        router.push('/')
      })
      .catch((error) => {
        errorMessage.value = error.response.data.detail;
      });
  };

  const logout = () => {
    user.value.loggedIn = false
  }

  const inboxq = async (state: boolean) => {
    if (state === false){
    await axios
    .get('http://127.0.0.1:8000/users/inboxq')
    .then((response) => {
      user.value.inbox = response.data.inbox
      loading.value=false
    })
  }
  }

  return {
    user,
    login,
    currentUser,
    errorMessage,
    users,
    logout,
    inboxq,
    loading
  };
}
