import { ref, reactive } from "vue";
import axios from "axios";
import router from "@/router/index.ts";

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
    history: History[]
    skills: {}[]
  };
  portfolio: boolean;
  projects: [Portfolio];
  profileCompleted: number
}

/** This is a description of the foo function. */
export default function UserWork() {
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
      history: [{date: '', description: ''}],
      skills: []
    },
    portfolio: false,
    projects: [{ id: 0, name: "", description: "", link: "" }],
    profileCompleted: null
  });

  const token = ref(localStorage.getItem("user_token"));
  const errorMessage = ref("");
  const loggedIn = ref("false");

  axios.defaults.headers.common["Authorization"] = `Bearer ${token.value}`;

  const login = (payload: any) => {
    axios
      .post("http://127.0.0.1:8000/users/login", payload)
      .then((response) => {
        localStorage.setItem("user_token", response.data.access_token);
        console.log(token.value);
        router.push("/profile");
      })
      .catch((error) => {
        errorMessage.value = error.response.data.detail;
      });
  };

  const currentUser = () => {
    axios
      .get("http://127.0.0.1:8000/users/user")
      .then((response) => {
        user.value = response.data;
      })
      .catch((error) => (errorMessage.value = error.response.data.detail));
  };



  return { user, login, currentUser, errorMessage };
}
