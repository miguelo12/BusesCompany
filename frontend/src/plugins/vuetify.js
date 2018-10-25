import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Vue from 'vue'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify, {
  iconfont: 'mdi',
  icons: {
    'product': 'mdi-dropbox',
    'support': 'mdi-lifebuoy',
    'steam': 'mdi-steam-box',
    'pc': 'mdi-desktop-classic',
    'xbox': 'mdi-xbox',
    'playstation': 'mdi-playstation',
    'switch': 'mdi-nintendo-switch',
    'insert_chart': 'insert_chart',
    'home': 'home',
    'info': 'info',
    'warning': 'warning',
    'delete': 'delete',
    'edit': 'edit',
    'directions_bus': 'directions_bus',
    'view_headline': 'view_headline',
    'dashboard': 'dashboard',
    'people': 'people',
    'place': 'place',
    'airline_seat_recline_normal': 'airline_seat_recline_normal'
  },
  options: {
    minifyTheme: function (css) {
      return process.env.NODE_ENV === 'production'
        ? css.replace(/[\s|\r\n|\r|\n]/g, '')
        : css
    },
    cspNonce: 'O5w4EdF2XsLmW9'
  }
})
