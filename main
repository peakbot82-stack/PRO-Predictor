# ============================================================
# APP PREDICTOR PRO - KIVY (VERSIÓN COMPLETA)
# ============================================================

import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.utils import get_color_from_hex
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

import random
from datetime import datetime

# ==================== COLORES ====================
COLORS = {
    'primary': '#6C63FF',
    'primary_dark': '#5A52D5',
    'secondary': '#03DAC6',
    'background': '#0F0F1A',
    'surface': '#1A1A2E',
    'surface_light': '#24243E',
    'text_primary': '#FFFFFF',
    'text_secondary': '#A0A0B8',
    'success': '#4CAF50',
    'error': '#F44336',
    'warning': '#FF9800',
}

# ==================== WIDGET CON BORDE REDONDEADO ====================
class RoundedButton(Button):
    def __init__(self, **kwargs):
        self.bg_color = kwargs.pop('bg_color', COLORS['primary'])
        self.radius = kwargs.pop('radius', [10])
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        self.border = (0, 0, 0, 0)
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        Clock.schedule_once(self.update_canvas, 0)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*get_color_from_hex(self.bg_color))
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)


class Toast(FloatLayout):
    def __init__(self, message, type='info', **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.8, None)
        self.height = 50
        self.pos_hint = {'center_x': 0.5, 'y': 0.05}
        self.opacity = 0
        
        colors = {
            'success': COLORS['success'],
            'error': COLORS['error'],
            'info': COLORS['primary'],
            'warning': COLORS['warning']
        }
        
        with self.canvas.before:
            Color(*get_color_from_hex(colors.get(type, COLORS['primary'])))
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        
        self.label = Label(
            text=message,
            font_size=14,
            bold=True,
            color=get_color_from_hex(COLORS['text_primary'])
        )
        self.add_widget(self.label)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        Clock.schedule_once(self.fade_in, 0.1)
        Clock.schedule_once(self.fade_out, 3)
        
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        
    def fade_in(self, dt):
        self.opacity = 1
        
    def fade_out(self, dt):
        self.opacity = 0
        Clock.schedule_once(self.remove_me, 0.5)
        
    def remove_me(self, dt):
        if self.parent:
            self.parent.remove_widget(self)


# ==================== PREDICTOR ====================
class Predictor:
    def __init__(self):
        self.mode = 'pro'
        self.running = False
        self.paused = False
        self.history = []
        self.stats = {
            'wins': 0,
            'losses': 0,
            'balance': 10.00,
            'win_rate': 0
        }
        self.current_color = None
        self.prediction = None
        self.last_result = None
        
    def start(self):
        self.running = True
        self.paused = False
        
    def pause(self):
        self.paused = not self.paused
        
    def stop(self):
        self.running = False
        self.paused = False
        
    def predict(self):
        if not self.running or self.paused:
            return None, None, None
            
        colors = ['🔴', '🔵']
        results = ['win', 'loss']
        
        color = random.choice(colors)
        prediction = random.choice(colors)
        result = random.choice(results)
        amount = 0.10
        
        if result == 'win':
            self.stats['wins'] += 1
            self.stats['balance'] += amount
        else:
            self.stats['losses'] += 1
            self.stats['balance'] -= amount
            
        total = self.stats['wins'] + self.stats['losses']
        self.stats['win_rate'] = round((self.stats['wins'] / total) * 100) if total > 0 else 0
        
        self.history.insert(0, {
            'color': color,
            'prediction': prediction,
            'result': result,
            'amount': amount,
            'time': datetime.now().strftime('%H:%M:%S')
        })
        if len(self.history) > 50:
            self.history.pop()
            
        self.current_color = color
        self.prediction = prediction
        self.last_result = result
        
        return color, prediction, result


# ==================== SCREEN LOGIN ====================
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()
        
    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=15)
        layout.bind(size=self._update_rect)
        
        with layout.canvas.before:
            Color(*get_color_from_hex(COLORS['background']))
            self.rect = Rectangle(pos=layout.pos, size=layout.size)
        
        logo = Label(
            text='🎰',
            font_size=80,
            color=get_color_from_hex(COLORS['text_primary'])
        )
        layout.add_widget(logo)
        
        title = Label(
            text='PRO Predictor',
            font_size=32,
            bold=True,
            color=get_color_from_hex(COLORS['primary'])
        )
        layout.add_widget(title)
        
        subtitle = Label(
            text='Inteligencia Artificial para Trading',
            font_size=14,
            color=get_color_from_hex(COLORS['text_secondary'])
        )
        layout.add_widget(subtitle)
        
        layout.add_widget(Widget(size_hint_y=0.1))
        
        self.email_input = TextInput(
            hint_text='📧 Correo Electrónico',
            font_size=16,
            size_hint_y=0.1,
            background_color=get_color_from_hex(COLORS['surface']),
            foreground_color=get_color_from_hex(COLORS['text_primary']),
            hint_text_color=get_color_from_hex(COLORS['text_secondary']),
            cursor_color=get_color_from_hex(COLORS['primary']),
            padding=[16, 12]
        )
        layout.add_widget(self.email_input)
        
        self.password_input = TextInput(
            hint_text='🔒 Contraseña',
            font_size=16,
            size_hint_y=0.1,
            background_color=get_color_from_hex(COLORS['surface']),
            foreground_color=get_color_from_hex(COLORS['text_primary']),
            hint_text_color=get_color_from_hex(COLORS['text_secondary']),
            cursor_color=get_color_from_hex(COLORS['primary']),
            padding=[16, 12],
            password=True
        )
        layout.add_widget(self.password_input)
        
        login_btn = RoundedButton(
            text='🚀 INICIAR SESIÓN',
            font_size=18,
            bold=True,
            size_hint_y=0.12,
            bg_color=COLORS['primary']
        )
        login_btn.bind(on_press=self.do_login)
        layout.add_widget(login_btn)
        
        register = Label(
            text='¿No tienes cuenta? Regístrate',
            font_size=14,
            color=get_color_from_hex(COLORS['text_secondary'])
        )
        layout.add_widget(register)
        
        footer = Label(
            text='💳 Aceptamos pagos con USDT',
            font_size=12,
            color=get_color_from_hex(COLORS['text_secondary'])
        )
        layout.add_widget(footer)
        
        self.add_widget(layout)
        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
    def do_login(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        
        if email and password:
            self.parent.current = 'dashboard'
            app = App.get_running_app()
            app.show_toast('🎉 ¡Bienvenido a PRO Predictor!', 'success')
        else:
            app = App.get_running_app()
            app.show_toast('❌ Completa todos los campos', 'error')


# ==================== SCREEN DASHBOARD ====================
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.predictor = Predictor()
        self.session_time = 0
        self.build_ui()
        self.update_clock = Clock.schedule_interval(self.update_stats, 0.5)
        self.session_clock = Clock.schedule_interval(self.update_session_time, 1)
        
    def build_ui(self):
        main_layout = BoxLayout(orientation='vertical', spacing=6, padding=10)
        main_layout.bind(size=self._update_rect)
        
        with main_layout.canvas.before:
            Color(*get_color_from_hex(COLORS['background']))
            self.rect = Rectangle(pos=main_layout.pos, size=main_layout.size)
        
        # ===== HEADER =====
        header = BoxLayout(size_hint_y=0.07, spacing=8)
        
        title = Label(
            text='🎰 PRO Predictor',
            font_size=20,
            bold=True,
            color=get_color_from_hex(COLORS['primary'])
        )
        header.add_widget(title)
        
        header_btns = BoxLayout(size_hint_x=0.3, spacing=4)
        
        config_btn = Button(
            text='⚙️',
            font_size=20,
            background_color=(0,0,0,0),
            color=get_color_from_hex(COLORS['text_secondary'])
        )
        config_btn.bind(on_press=self.show_config)
        header_btns.add_widget(config_btn)
        
        logout_btn = Button(
            text='🚪',
            font_size=20,
            background_color=(0,0,0,0),
            color=get_color_from_hex(COLORS['text_secondary'])
        )
        logout_btn.bind(on_press=self.do_logout)
        header_btns.add_widget(logout_btn)
        
        header.add_widget(header_btns)
        main_layout.add_widget(header)
        
        # ===== STATS =====
        stats_grid = GridLayout(cols=4, spacing=6, size_hint_y=0.12)
        
        stats_data = [
            ('💰', 'balance', '$10.00'),
            ('📊', 'win_rate', '0%'),
            ('🏆', 'wins_losses', '0/0'),
            ('⏱️', 'session', '00:00:00')
        ]
        
        self.stats_labels = {}
        for icon, key, default in stats_data:
            box = BoxLayout(orientation='vertical', spacing=1)
            box.add_widget(Label(text=icon, font_size=22))
            label = Label(
                text=default,
                font_size=16,
                bold=True,
                color=get_color_from_hex(COLORS['text_primary'])
            )
            box.add_widget(label)
            self.stats_labels[key] = label
            stats_grid.add_widget(box)
            
        main_layout.add_widget(stats_grid)
        
        # ===== PREDICCIÓN =====
        pred_box = BoxLayout(
            orientation='vertical',
            size_hint_y=0.30,
            padding=12,
            spacing=4
        )
        pred_box.bind(pos=self._update_pred_box, size=self._update_pred_box)
        
        pred_header = BoxLayout(size_hint_y=0.2)
        pred_header.add_widget(Label(
            text='🎯 PREDICCIÓN EN VIVO',
            font_size=13,
            bold=True,
            color=get_color_from_hex(COLORS['text_secondary'])
        ))
        self.status_label = Label(
            text='INACTIVO',
            font_size=12,
            bold=True,
            color=get_color_from_hex(COLORS['error'])
        )
        pred_header.add_widget(self.status_label)
        pred_box.add_widget(pred_header)
        
        color_layout = BoxLayout(size_hint_y=0.55, spacing=15)
        
        self.last_color = Label(
            text='?',
            font_size=45,
            color=get_color_from_hex(COLORS['text_secondary'])
        )
        color_layout.add_widget(self.last_color)
        
        color_layout.add_widget(Label(
            text='→',
            font_size=28,
            color=get_color_from_hex(COLORS['text_secondary'])
        ))
        
        self.pred_color = Label(
            text='?',
            font_size=45,
            color=get_color_from_hex(COLORS['text_secondary'])
        )
        color_layout.add_widget(self.pred_color)
        
        pred_box.add_widget(color_layout)
        
        self.result_label = Label(
            text='⏳ Esperando...',
            font_size=16,
            bold=True,
            color=get_color_from_hex(COLORS['warning'])
        )
        pred_box.add_widget(self.result_label)
        
        main_layout.add_widget(pred_box)
        
        # ===== CONTROLES =====
        control_layout = BoxLayout(size_hint_y=0.08, spacing=6)
        
        self.start_btn = RoundedButton(
            text='▶ INICIAR',
            font_size=13,
            bold=True,
            bg_color=COLORS['success'],
            radius=[8]
        )
        self.start_btn.bind(on_press=self.start_bot)
        control_layout.add_widget(self.start_btn)
        
        self.pause_btn = RoundedButton(
            text='⏸ PAUSAR',
            font_size=13,
            bold=True,
            bg_color=COLORS['warning'],
            radius=[8],
            disabled=True
        )
        self.pause_btn.bind(on_press=self.pause_bot)
        control_layout.add_widget(self.pause_btn)
        
        self.stop_btn = RoundedButton(
            text='⏹ DETENER',
            font_size=13,
            bold=True,
            bg_color=COLORS['error'],
            radius=[8],
            disabled=True
        )
        self.stop_btn.bind(on_press=self.stop_bot)
        control_layout.add_widget(self.stop_btn)
        
        main_layout.add_widget(control_layout)
        
        # ===== MODO SELECTOR =====
        mode_box = BoxLayout(
            orientation='vertical',
            size_hint_y=0.08,
            spacing=2,
            padding=[0, 4]
        )
        
        mode_box.add_widget(Label(
            text='🎲 MODO',
            font_size=11,
            color=get_color_from_hex(COLORS['text_secondary'])
        ))
        
        mode_grid = GridLayout(cols=5, spacing=3, size_hint_y=0.7)
        modes = [
            ('🏆 PRO', 'pro'),
            ('🔧 HACK', 'hack'),
            ('⛰️ PEAK', 'peak'),
            ('🎯 CAZADOR', 'cazador'),
            ('📊 TEND', 'tendencial')
        ]
        
        self.mode_buttons = {}
        for text, mode in modes:
            btn = RoundedButton(
                text=text,
                font_size=9,
                bold=True,
                bg_color=COLORS['surface_light'],
                color=get_color_from_hex(COLORS['text_secondary']),
                radius=[8]
            )
            btn.mode = mode
            btn.bind(on_press=self.select_mode)
            mode_grid.add_widget(btn)
            self.mode_buttons[mode] = btn
            
        self.mode_buttons['pro'].bg_color = COLORS['primary']
        self.mode_buttons['pro'].color = get_color_from_hex(COLORS['text_primary'])
        
        mode_box.add_widget(mode_grid)
        main_layout.add_widget(mode_box)
        
        # ===== HISTORIAL =====
        hist_box = BoxLayout(
            orientation='vertical',
            size_hint_y=0.22,
            spacing=2
        )
        
        hist_header = BoxLayout(size_hint_y=0.2)
        hist_header.add_widget(Label(
            text='📋 HISTORIAL',
            font_size=11,
            bold=True,
            color=get_color_from_hex(COLORS['text_secondary'])
        ))
        hist_header.add_widget(Label(size_hint_x=0.3))
        hist_header.add_widget(Button(
            text='Ver todos',
            font_size=10,
            background_color=(0,0,0,0),
            color=get_color_from_hex(COLORS['primary']),
            size_hint_x=0.3
        ))
        hist_box.add_widget(hist_header)
        
        scroll = ScrollView(size_hint_y=0.8)
        self.history_list = BoxLayout(orientation='vertical', spacing=1, size_hint_y=None)
        self.history_list.bind(minimum_height=self.history_list.setter('height'))
        scroll.add_widget(self.history_list)
        hist_box.add_widget(scroll)
        
        main_layout.add_widget(hist_box)
        
        self.add_widget(main_layout)
        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
    def _update_pred_box(self, instance, value):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(*get_color_from_hex(COLORS['surface']))
            RoundedRectangle(pos=instance.pos, size=instance.size, radius=[12])
        
    def update_stats(self, dt):
        stats = self.predictor.stats
        self.stats_labels['balance'].text = f'${stats["balance"]:.2f}'
        self.stats_labels['win_rate'].text = f'{stats["win_rate"]}%'
        self.stats_labels['wins_losses'].text = f'{stats["wins"]}/{stats["losses"]}'
        
        if self.predictor.running:
            if self.predictor.paused:
                self.status_label.text = 'PAUSADO'
                self.status_label.color = get_color_from_hex(COLORS['warning'])
            else:
                self.status_label.text = 'ACTIVO'
                self.status_label.color = get_color_from_hex(COLORS['success'])
        else:
            self.status_label.text = 'INACTIVO'
            self.status_label.color = get_color_from_hex(COLORS['error'])
            
        self.update_history()
        
    def update_session_time(self, dt):
        if self.predictor.running and not self.predictor.paused:
            self.session_time += 1
            h = self.session_time // 3600
            m = (self.session_time % 3600) // 60
            s = self.session_time % 60
            self.stats_labels['session'].text = f'{h:02d}:{m:02d}:{s:02d}'
            
    def update_history(self):
        self.history_list.clear_widgets()
        for item in self.predictor.history[:8]:
            row = BoxLayout(size_hint_y=None, height=28, spacing=4, padding=[4, 2])
            
            color_text = item['color']
            result_text = '✅ WIN' if item['result'] == 'win' else '❌ LOSS'
            result_color = COLORS['success'] if item['result'] == 'win' else COLORS['error']
            sign = '+' if item['result'] == 'win' else '-'
            
            row.add_widget(Label(text=color_text, font_size=16, size_hint_x=0.12))
            row.add_widget(Label(
                text=result_text,
                font_size=10,
                bold=True,
                color=get_color_from_hex(result_color),
                size_hint_x=0.28
            ))
            row.add_widget(Label(
                text=f'{sign}${item["amount"]:.2f}',
                font_size=10,
                bold=True,
                color=get_color_from_hex(result_color),
                size_hint_x=0.25
            ))
            row.add_widget(Label(
                text=item['time'],
                font_size=9,
                color=get_color_from_hex(COLORS['text_secondary']),
                size_hint_x=0.25
            ))
            
            self.history_list.add_widget(row)
            
    # ===== BOT CONTROLS =====
    def start_bot(self, instance):
        self.predictor.start()
        self.start_btn.disabled = True
        self.start_btn.text = '▶ EJECUTANDO'
        self.pause_btn.disabled = False
        self.stop_btn.disabled = False
        self.session_time = 0
        
        if not hasattr(self, 'predict_clock'):
            self.predict_clock = Clock.schedule_interval(self.make_prediction, 2.5)
            
        app = App.get_running_app()
        app.show_toast('🚀 Bot iniciado en modo ' + self.predictor.mode.upper(), 'success')
        
    def pause_bot(self, instance):
        self.predictor.pause()
        if self.predictor.paused:
            instance.text = '▶ REANUDAR'
            app = App.get_running_app()
            app.show_toast('⏸️ Bot pausado', 'info')
        else:
            instance.text = '⏸ PAUSAR'
            app = App.get_running_app()
            app.show_toast('▶️ Bot reanudado', 'info')
            
    def stop_bot(self, instance):
        self.predictor.stop()
        self.start_btn.disabled = False
        self.start_btn.text = '▶ INICIAR'
        self.pause_btn.disabled = True
        self.stop_btn.disabled = True
        self.pause_btn.text = '⏸ PAUSAR'
        
        if hasattr(self, 'predict_clock'):
            self.predict_clock.cancel()
            delattr(self, 'predict_clock')
            
        app = App.get_running_app()
        app.show_toast('⏹️ Bot detenido', 'warning')
        
    def make_prediction(self, dt):
        color, prediction, result = self.predictor.predict()
        if color:
            color_hex = COLORS['error'] if color == '🔴' else COLORS['primary']
            self.last_color.text = color
            self.last_color.color = get_color_from_hex(color_hex)
            
            pred_hex = COLORS['error'] if prediction == '🔴' else COLORS['primary']
            self.pred_color.text = prediction
            self.pred_color.color = get_color_from_hex(pred_hex)
            
            if result == 'win':
                self.result_label.text = '✅ WIN'
                self.result_label.color = get_color_from_hex(COLORS['success'])
            else:
                self.result_label.text = '❌ LOSS'
                self.result_label.color = get_color_from_hex(COLORS['error'])
                
    # ===== MODO SELECTOR =====
    def select_mode(self, instance):
        mode = instance.mode
        self.predictor.mode = mode
        
        for m, btn in self.mode_buttons.items():
            btn.bg_color = COLORS['surface_light']
            btn.color = get_color_from_hex(COLORS['text_secondary'])
            
        instance.bg_color = COLORS['primary']
        instance.color = get_color_from_hex(COLORS['text_primary'])
        
        app = App.get_running_app()
        app.show_toast(f'🎯 Modo: {mode.upper()}', 'info')
        
    # ===== CONFIGURACIÓN =====
    def show_config(self, instance):
        app = App.get_running_app()
        app.show_config_popup()
        
    def do_logout(self, instance):
        self.predictor.stop()
        if hasattr(self, 'predict_clock'):
            self.predict_clock.cancel()
            delattr(self, 'predict_clock')
        self.parent.current = 'login'
        app = App.get_running_app()
        app.show_toast('👋 Sesión cerrada', 'info')


# ==================== APP PRINCIPAL ====================
class PredictorApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex(COLORS['background'])
        
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(DashboardScreen(name='dashboard'))
        
        self.toast_container = None
        self.current_popup = None
        
        return self.sm
    
    def show_toast(self, message, type='info'):
        screen = self.sm.current_screen
        toast = Toast(message, type)
        screen.add_widget(toast)
        
    def show_config_popup(self):
        content = BoxLayout(orientation='vertical', padding=16, spacing=10)
        content.size_hint = (0.85, 0.75)
        
        content.add_widget(Label(
            text='⚙️ CONFIGURACIÓN',
            font_size=18,
            bold=True,
            color=get_color_from_hex(COLORS['text_primary']),
            size_hint_y=0.08
        ))
        
        fields = [
            ('💰 Apuesta Inicial', '0.10'),
            ('📈 Apuesta Máxima', '10.00'),
            ('🛑 Stop Loss', '5'),
            ('🔄 Monto Reinicio', '0.10'),
            ('⏸️ Max Pausas', '2'),
            ('🎯 Take Profit', '0.00')
        ]
        
        self.config_inputs = {}
        for label, default in fields:
            box = BoxLayout(orientation='vertical', size_hint_y=0.08)
            box.add_widget(Label(
                text=label,
                font_size=10,
                color=get_color_from_hex(COLORS['text_secondary']),
                size_hint_y=0.25
            ))
            inp = TextInput(
                text=default,
                font_size=13,
                background_color=get_color_from_hex(COLORS['background']),
                foreground_color=get_color_from_hex(COLORS['text_primary']),
                cursor_color=get_color_from_hex(COLORS['primary']),
                padding=[10, 4],
                size_hint_y=0.75
            )
            box.add_widget(inp)
            content.add_widget(box)
            self.config_inputs[label] = inp
            
        strat_box = BoxLayout(orientation='vertical', size_hint_y=0.08)
        strat_box.add_widget(Label(
            text='🎲 Gestión',
            font_size=10,
            color=get_color_from_hex(COLORS['text_secondary']),
            size_hint_y=0.25
        ))
        strat_layout = BoxLayout(size_hint_y=0.75, spacing=6)
        for strat in ['Martingala', 'Agresivo']:
            btn = RoundedButton(
                text=strat,
                font_size=11,
                bold=True,
                bg_color=COLORS['surface_light'],
                color=get_color_from_hex(COLORS['text_secondary']),
                radius=[8]
            )
            btn.strategy = strat
            btn.bind(on_press=self.select_strategy)
            strat_layout.add_widget(btn)
        strat_box.add_widget(strat_layout)
        content.add_widget(strat_box)
        
        save_btn = RoundedButton(
            text='💾 GUARDAR',
            font_size=14,
            bold=True,
            bg_color=COLORS['primary'],
            size_hint_y=0.08,
            radius=[8]
        )
        save_btn.bind(on_press=self.save_config)
        content.add_widget(save_btn)
        
        popup = Popup(
            title='',
            content=content,
            size_hint=(0.9, 0.8),
            background='',
            separator_color=(0,0,0,0)
        )
        
        with popup.canvas.before:
            Color(*get_color_from_hex(COLORS['surface']))
            RoundedRectangle(pos=popup.pos, size=popup.size, radius=[16])
            
        popup.open()
        self.current_popup = popup
        
    def select_strategy(self, instance):
        for child in instance.parent.children:
            if hasattr(child, 'bg_color'):
                child.bg_color = COLORS['surface_light']
                child.color = get_color_from_hex(COLORS['text_secondary'])
        instance.bg_color = COLORS['primary']
        instance.color = get_color_from_hex(COLORS['text_primary'])
        
    def save_config(self, instance):
        config = {}
        for label, inp in self.config_inputs.items():
            config[label] = inp.text
        self.show_toast('✅ Configuración guardada', 'success')
        if self.current_popup:
            self.current_popup.dismiss()


# ==================== EJECUTAR ====================
if __name__ == '__main__':
    PredictorApp().run()
