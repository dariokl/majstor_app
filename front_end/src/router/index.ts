import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import LoginView from "../views/LoginView.vue";
import Profile from '../views/Profile.vue';
import Qsearch from '../views/Qsearch.vue';
import Inbox from '../views/InboxV.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/q/:search',
    name: 'Search',
    component: Qsearch,
  },
  {
    path: '/inbox',
    name: 'Inbox',
    component: Inbox
  }

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
