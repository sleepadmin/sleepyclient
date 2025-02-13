import requests
import pyMeow as pm
import pymem, pymem.process, keyboard, time, os 
from os import system, name
from win32gui import GetWindowText, GetForegroundWindow
from random import uniform
import threading
import webbrowser
from requests import get
import shutil
from pypresence import Presence
from colorama import Fore
from win32api import GetKeyState
import os
import re
import subprocess
import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
import requests
import webbrowser
import shutil
import platform
from colorama import Fore, Style, init
import ctypes

from pynput.mouse import Button, Controller

mouse = Controller()

OUTPUT_PATH = Path(__file__).resolve().parent
ASSETS_PATH = OUTPUT_PATH / "assets"

init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("Sleep Client")

columns = shutil.get_terminal_size().columns

client_id = "1333575446473871430"
RPC = Presence(client_id)

box_esp = True
skeleton_esp = True
head_esp = True
triggerbot = True
tracers = True
esp_global = True
triggerKey = 0x05
rich_presence = False
goonermode = False
tis = False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def default():
    global box_esp, skeleton_esp, head_esp, triggerbot, esp_global, tracers, tis
    print(f"{Fore.GREEN}True: On\n{Fore.RED}False: Off{Fore.RESET}")
    print()
    print(f"0 --Global ESP: {esp_global}")
    print(f"1 --Box ESP: {box_esp}")
    print(f"2 --Skeleton ESP: {skeleton_esp}")
    print(f"3 --Head ESP: {head_esp}")
    print(f"4 --Triggerbot: {triggerbot}")
    print(f"5 --Tracers: {tracers}")
    print("")
    print("6 --Change triggerkey")
    print(f"7 --Triggerbot spray: {tis} (NOT RECOMMENDED)")
    if triggerKey == 0x06:
        print("? --Trigger key: MouseButton 5")
    elif triggerKey == 0x05:
        print("? --Trigger key: MouseButton 4")
    else:
        print(f"? --Trigger key: {triggerKey}")
    print("")
    print(f"8 --Rich Presence: {rich_presence}")
    print(f"help --Explains what each thing does")
    print("9 --Launch Sleep Client")
    print()


def GoonerDefault():
    global box_esp, skeleton_esp, head_esp, triggerbot, esp_global, tracers, tis
    print(f"{Fore.GREEN}True: On\n{Fore.RED}False: Off{Fore.RESET}")
    print()
    print(f"0 --Global ESP: {esp_global} {Fore.YELLOW}(If off no ESP will be shown){Fore.RESET}")
    print(f"1 --Box ESP: {box_esp} {Fore.YELLOW}(Adds a box around player){Fore.RESET}")
    print(f"2 --Skeleton ESP: {skeleton_esp} {Fore.YELLOW}(Displays player skeleton){Fore.RESET}")
    print(f"3 --Head ESP: {head_esp} {Fore.YELLOW}(Adds a circle around enemy head){Fore.RESET}")
    print(f"4 --Triggerbot: {triggerbot} {Fore.YELLOW}({('MouseButton 4' if triggerKey == 0x05 else 'MouseButton 5' if triggerKey == 0x06 else triggerKey)} auto-fires when an enemy is in your crosshair){Fore.RESET}")
    print(f"5 --Tracers: {tracers} {Fore.YELLOW}(Adds a line to the enemy){Fore.RESET}")
    print()
    print(f"6 --Change triggerkey {Fore.YELLOW}(Change your triggerkey){Fore.RED}")
    print(f"7 --Triggerbot spray: {tis} {Fore.YELLOW}(Makes the triggerbot spray) {Fore.RED}[NOT RECOMMENDED]{Fore.RESET}")
    if triggerKey == 0x06:
        print(f"? --Trigger key: MouseButton 5 {Fore.YELLOW}(This is the key you hold for auto-fire){Fore.RESET}")
    elif triggerKey == 0x05:
        print(f"? --Trigger key: MouseButton 4")
    else:
        print(f"? --Trigger key: {triggerKey}")
    print("")
    print(f"8 --Rich Presence: {rich_presence} {Fore.YELLOW}(Makes your discord activity Sleep Client){Fore.RESET}")
    print(f"h --Explains what each thing does")
    print(f"9 --Launch Sleep Client {Fore.GREEN}(Starts up Sleep Client with your desired configuration!){Fore.RESET}")
    print()

def change_trigger_key():
    global triggerKey
    print("Press any key to set it as the new trigger key.")
    time.sleep(0.1)
    event = keyboard.read_event(suppress=True)
    triggerKey = event.name
    print(f"Trigger key changed to: {triggerKey}")

def choices():
    global box_esp, skeleton_esp, head_esp, triggerbot, esp_global, rich_presence, key, tracers, tis, goonermode
    clear()
    print("Brought to you by Fundet & Geoloage 💎".center(columns).rstrip())
    print(f"{Fore.YELLOW}        // // ver 0.2.0 // //{Fore.RESET}".center(columns).rstrip())
    if goonermode == True:
        GoonerDefault()
    else:
        default()

    enable = input("Choose an option: ")
    if enable == "1":
        box_esp = not box_esp
        choices()
    elif enable == "2":
        skeleton_esp = not skeleton_esp
        choices()
    elif enable == "3":
        head_esp = not head_esp
        choices()
    elif enable == "4":
        triggerbot = not triggerbot
        choices()
    elif enable == "0":
        esp_global = not esp_global
        choices()
    elif enable == "5":
        tracers = not tracers
        choices()
    elif enable == "6":
        choose_trigger()
    elif enable == "7":
        tis = not tis
        choices()
    elif enable == "8":
        rich_presence = not rich_presence
        choices()
    elif enable == "h" or enable == "H":
        goonermode = not goonermode
        choices()
    elif enable == "9":
        esp = CS2Esp(box_esp, skeleton_esp, head_esp)
    else:
        print("Invalid input")
        input("Press Enter to continue...")
        choices()

def choose_trigger():
    global triggerKey
    clear()
    print("Brought to you by Fundet & Geoloage 💎".center(columns).rstrip())
    print(f"{Fore.YELLOW}        // // ver 0.2.0 // //{Fore.RESET}".center(columns).rstrip())
    print("1 --MouseButton5")
    print("2 --MouseButton4")
    print("3 --Keyboard button")
    print("4 --Back")
    print()

    tc = input("Choose an option: ")

    if tc == "1":
        triggerKey = 0x06
        choices()
    if tc == "2":
        triggerKey = 0x05
        choices()
    if tc == "3":
        change_trigger_key()
        choices()
    if tc == "4":
        choices()
    
class Offsets:
    dwViewMatrix = 27797312
    dwEntityList = 27358920
    dwLocalPlayerController = 27689168
    dwLocalPlayerPawn = 25607672
    m_pBoneArray = 496

    BONE_POSITIONS = {
        "head": 6,
        "chest": 2,
        "left_hand": 10,
        "right_hand": 15,
        "left_leg": 23,
        "right_leg": 26,
        "left_foot": 24,
        "left_shoulder": 8,
        "right_foot": 27,
        "right_shoulder": 13,
        "left_arm": 9,
        "right_arm": 14,
        "neck": 5,
    }


    offset = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
    client = get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()

    dwEntityList = offset["client.dll"]["dwEntityList"]
    dwViewMatrix = offset["client.dll"]["dwViewMatrix"]
    dwLocalPlayerPawn = offset["client.dll"]["dwLocalPlayerPawn"]
    dwLocalPlayerController = offset["client.dll"]["dwLocalPlayerController"]
    m_iszPlayerName = client["client.dll"]["classes"]["CBasePlayerController"]["fields"]["m_iszPlayerName"]
    m_iHealth = client["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iHealth"]
    m_iTeamNum = client["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_iTeamNum"]
    m_vOldOrigin = client["client.dll"]["classes"]["C_BasePlayerPawn"]["fields"]["m_vOldOrigin"]
    m_pGameSceneNode = client["client.dll"]["classes"]["C_BaseEntity"]["fields"]["m_pGameSceneNode"]
    m_hPlayerPawn = client["client.dll"]["classes"]["CCSPlayerController"]["fields"]["m_hPlayerPawn"]
    m_iIDEntIndex = client["client.dll"]["classes"]["C_CSPlayerPawnBase"]["fields"]["m_iIDEntIndex"]

mouse = Controller()

dwEntityList = Offsets.dwEntityList
dwLocalPlayerPawn = Offsets.dwLocalPlayerPawn
m_iIDEntIndex = Offsets.m_iIDEntIndex
m_iTeamNum = Offsets.m_iTeamNum
m_iHealth = Offsets.m_iHealth


class Colors:
    orange = pm.get_color("orange")
    black = pm.get_color("black")
    cyan = pm.get_color("cyan")
    white = pm.get_color("white")
    green = pm.get_color("green")
    grey = pm.fade_color(pm.get_color("#242625"), 0.7)


class Skeleton:
    bone_pairs = [
        ("head", "chest"),
        ("right_foot", "right_leg", "chest"),
        ("left_foot", "left_leg", "chest"),
        ("right_hand", "right_arm", "right_shoulder", "neck"),
        ("left_hand", "left_arm", "left_shoulder", "neck"),
    ]


class Entity:
    def __init__(self, ptr, pawn_ptr, proc):
        self.ptr = ptr
        self.pawn_ptr = pawn_ptr
        self.proc = proc
        self.pos2d = None
        self.head_pos2d = None

    @property
    def name(self):
        return pm.r_string(self.proc, self.ptr + Offsets.m_iszPlayerName)

    @property
    def health(self):
        return pm.r_int(self.proc, self.pawn_ptr + Offsets.m_iHealth)

    @property
    def team(self):
        return pm.r_int(self.proc, self.pawn_ptr + Offsets.m_iTeamNum)

    @property
    def pos(self):
        return pm.r_vec3(self.proc, self.pawn_ptr + Offsets.m_vOldOrigin)

    @property
    def dormant(self):
        return pm.r_bool(self.proc, self.pawn_ptr + Offsets.m_bDormant)

    def bone_pos(self, bone):
        game_scene = pm.r_int64(self.proc, self.pawn_ptr + Offsets.m_pGameSceneNode)
        bone_array_ptr = pm.r_int64(self.proc, game_scene + Offsets.m_pBoneArray)
        bone_pos_address = bone_array_ptr + bone * 32
        bone_position = pm.r_vec3(self.proc, bone_pos_address)
        return bone_position

    def wts(self, view_matrix):
        try:
            
            self.pos2d = pm.world_to_screen(view_matrix, self.pos, 1)
            self.head_pos2d = pm.world_to_screen(view_matrix, self.bone_pos(Offsets.BONE_POSITIONS["head"]), 1)
        except:
            return False
        return True

    def skeleton(self, view_matrix):
        skeleton_positions = {}
        for part, bone_id in Offsets.BONE_POSITIONS.items():
            try:
                bone_world = self.bone_pos(bone_id)
                if not bone_world:
                    continue
                bone_screen = pm.world_to_screen(view_matrix, bone_world, 1)
                skeleton_positions[part] = bone_screen
            except:
                continue
        return skeleton_positions


def triggerbot_logic(pm, client):
    global mouse
    time.sleep(0.001)
    print(f"[-] TriggerBot started.")
    if triggerKey == 0x06:
        print("[-] Trigger key: MouseButton 5")
    elif triggerKey == 0x05:
        print("[-] Trigger key: MouseButton 4")
    else:
        print(f"[-] Trigger key: {triggerKey}")
    try:
        pm = pymem.Pymem("cs2.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    except:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Please open CSGO 2!")
        exit()

    while True:
        try:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike 2":
                time.sleep(0.01)
                continue

            if keyboard.is_pressed(triggerKey):
                player = pm.read_longlong(client + dwLocalPlayerPawn)
                entityId = pm.read_int(player + m_iIDEntIndex)

                if entityId > 0:
                    entList = pm.read_longlong(client + dwEntityList)

                    entEntry = pm.read_longlong(entList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.read_longlong(entEntry + 120 * (entityId & 0x1FF))

                    entityTeam = pm.read_int(entity + m_iTeamNum)
                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeam != playerTeam:
                        entityHp = pm.read_int(entity + m_iHealth)
                        if entityHp > 0:
                            time.sleep(uniform(0.01, 0.03))
                            mouse.press(Button.left)
                            time.sleep(uniform(0.01, 0.05))
                            mouse.release(Button.left)

                time.sleep(0.03)
            else:
                time.sleep(0.01)

        except KeyboardInterrupt:
            print("[!] TriggerBot stopped.")
            break
        except Exception as e:
            print(f"[!] Error in TriggerBot loop: {e}")
            time.sleep(0.01)

def triggerbot_logic2(pm, client):
    global mouse
    time.sleep(0.001)
    print(f"[-] TriggerBot started.")
    if triggerKey == 0x06:
        print("[-] Trigger key: MouseButton 5")
    elif triggerKey == 0x05:
        print("[-] Trigger key: MouseButton 4")
    else:
        print(f"[-] Trigger key: {triggerKey}")
    try:
        pm = pymem.Pymem("cs2.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    except:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Please open CSGO 2!")
        exit()

    while True:
        try:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike 2":
                continue

            if GetKeyState(triggerKey) < 0:
                player = pm.read_longlong(client + dwLocalPlayerPawn)
                entityId = pm.read_int(player + m_iIDEntIndex)

                if entityId > 0:
                    entList = pm.read_longlong(client + dwEntityList)

                    entEntry = pm.read_longlong(entList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.read_longlong(entEntry + 120 * (entityId & 0x1FF))

                    entityTeam = pm.read_int(entity + m_iTeamNum)
                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeam != playerTeam:
                        entityHp = pm.read_int(entity + m_iHealth)
                        if entityHp > 0:
                            time.sleep(uniform(0.01, 0.03))
                            mouse.press(Button.left)
                            time.sleep(uniform(0.01, 0.05))
                            mouse.release(Button.left)

                time.sleep(0.03)
            else:
                time.sleep(0.01)

        except KeyboardInterrupt:
            print("[!] TriggerBot stopped.")
            break
        except Exception as e:
            print(f"[!] Error in TriggerBot loop: {e}")
            time.sleep(0.01)

def tislogic2(pm, client):
    global mouse
    time.sleep(0.001)
    print(f"[-] TriggerBot started.")
    if triggerKey == 0x06:
        print("[-] Trigger key: MouseButton 5")
    elif triggerKey == 0x05:
        print("[-] Trigger key: MouseButton 4")
    else:
        print(f"[-] Trigger key: {triggerKey}")
    try:
        pm = pymem.Pymem("cs2.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    except:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Please open CSGO 2!")
        exit()

    while True:
        try:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike 2":
                continue

            if GetKeyState(triggerKey) < 0:
                player = pm.read_longlong(client + dwLocalPlayerPawn)
                entityId = pm.read_int(player + m_iIDEntIndex)

                if entityId > 0:
                    entList = pm.read_longlong(client + dwEntityList)

                    entEntry = pm.read_longlong(entList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.read_longlong(entEntry + 120 * (entityId & 0x1FF))

                    entityTeam = pm.read_int(entity + m_iTeamNum)
                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeam != playerTeam:
                        entityHp = pm.read_int(entity + m_iHealth)
                        if entityHp > 0:
                            mouse.press(Button.left)
                            mouse.release(Button.left)
            else:
                time.sleep(0.01)

        except KeyboardInterrupt:
            print("[!] TriggerBot stopped.")
            break
        except Exception as e:
            print(f"[!] Error in TriggerBot loop: {e}")
            time.sleep(0.01)

def tislogic(pm, client):
    global mouse
    time.sleep(0.001)
    print(f"[-] TriggerBot started.")
    if triggerKey == 0x06:
        print("[-] Trigger key: MouseButton 5")
    elif triggerKey == 0x05:
        print("[-] Trigger key: MouseButton 4")
    else:
        print(f"[-] Trigger key: {triggerKey}")
    try:
        pm = pymem.Pymem("cs2.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    except:
        os.system("cls") if os.name == "nt" else os.system("clear")
        print("Please open CSGO 2!")
        exit()

    while True:
        try:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike 2":
                time.sleep(0.01)
                continue

            if keyboard.is_pressed(triggerKey):
                player = pm.read_longlong(client + dwLocalPlayerPawn)
                entityId = pm.read_int(player + m_iIDEntIndex)

                if entityId > 0:
                    entList = pm.read_longlong(client + dwEntityList)

                    entEntry = pm.read_longlong(entList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.read_longlong(entEntry + 120 * (entityId & 0x1FF))

                    entityTeam = pm.read_int(entity + m_iTeamNum)
                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeam != playerTeam:
                        entityHp = pm.read_int(entity + m_iHealth)
                        if entityHp > 0:
                            mouse.press(Button.left)
                            mouse.release(Button.left)
            else:
                time.sleep(0.01)

        except KeyboardInterrupt:
            print("[!] TriggerBot stopped.")
            break
        except Exception as e:
            print(f"[!] Error in TriggerBot loop: {e}")
            time.sleep(0.01)

class CS2Esp:
    def __init__(self, box_esp, skeleton_esp, head_esp):
        self.proc = pm.open_process("cs2.exe")
        self.mod = pm.get_module(self.proc, "client.dll")["base"]

        self.box_esp = box_esp
        self.skeleton_esp = skeleton_esp
        self.head_esp = head_esp

        offsets_name = ["dwViewMatrix", "dwEntityList", "dwLocalPlayerController", "dwLocalPlayerPawn"]
        offsets = requests.get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/offsets.json").json()
        [setattr(Offsets, k, offsets["client.dll"][k]) for k in offsets_name]

        client_dll_name = {
            "m_iIDEntIndex": "C_CSPlayerPawnBase",
            "m_hPlayerPawn": "CCSPlayerController",
            "m_fFlags": "C_BaseEntity",
            "m_iszPlayerName": "CBasePlayerController",
            "m_iHealth": "C_BaseEntity",
            "m_iTeamNum": "C_BaseEntity",
            "m_vOldOrigin": "C_BasePlayerPawn",
            "m_pGameSceneNode": "C_BaseEntity",
            "m_bDormant": "CGameSceneNode",
        }
        clientDll = requests.get("https://raw.githubusercontent.com/a2x/cs2-dumper/main/output/client_dll.json").json()
        [setattr(Offsets, k, clientDll["client.dll"]["classes"][client_dll_name[k]]["fields"][k]) for k in client_dll_name]

        if rich_presence:
            RPC.connect()
            RPC.update(state="discord.gg/39cYzXPYcc")
        else:
            print("#3")

        if esp_global:
            threading.Thread(target=self.run).start()
        else:
            print("#2")

        if triggerbot and triggerKey == 0x05 or triggerKey == 0x06:
            threading.Thread(target=triggerbot_logic2, args=(self.proc, self.mod)).start()
        elif triggerbot and tis and triggerKey == 0x05 or triggerKey == 0x06:
            threading.Thread(target=tislogic2, args=(self.proc, self.mod)).start()
        elif triggerKey and tis:
            threading.Thread(target=tislogic, args=(self.proc, self.mod)).start()
        elif triggerbot:
            threading.Thread(target=triggerbot_logic, args=(self.proc, self.mod)).start()
        else:
            print("#1")


    def it_entities(self):
        ent_list = pm.r_int64(self.proc, self.mod + Offsets.dwEntityList)
        local = pm.r_int64(self.proc, self.mod + Offsets.dwLocalPlayerController)

        for i in range(1, 65):
            try:
                entry_ptr = pm.r_int64(self.proc, ent_list + (8 * (i & 0x7FFF) >> 9) + 16)
                controller_ptr = pm.r_int64(self.proc, entry_ptr + 120 * (i & 0x1FF))

                if controller_ptr == local:
                    continue
                
                controller_pawn_ptr = pm.r_int64(self.proc, controller_ptr + Offsets.m_hPlayerPawn)
                list_entry_ptr = pm.r_int64(self.proc, ent_list + 0x8 * ((controller_pawn_ptr & 0x7FFF) >> 9) + 16)
                pawn_ptr = pm.r_int64(self.proc, list_entry_ptr + 120 * (controller_pawn_ptr & 0x1FF))
            except:
                continue

            yield Entity(controller_ptr, pawn_ptr, self.proc)



    def run(self):
        pm.overlay_init("Counter-Strike 2", fps=144)
        print("[-] ESP started.")

        def draw_health_bar(ent, color, width, head):
            bar_height = head + 5
            bar_width = 5
            bar_x = ent.head_pos2d["x"] - width / 2 - 10
            bar_y = ent.head_pos2d["y"] - head / 10

            health_percentage = ent.health / 100

            pm.draw_rectangle(bar_x, bar_y, bar_width, bar_height, Colors.grey)

            pm.draw_rectangle(
                bar_x,
                bar_y + bar_height * (1 - health_percentage),
                bar_width,
                bar_height * health_percentage,
                color,
            )

        while pm.overlay_loop():
            try:
                view_matrix = pm.r_floats(self.proc, self.mod + Offsets.dwViewMatrix, 16)

                pm.begin_drawing()
                pm.draw_fps(0, 0)

                for ent in self.it_entities():
                    if ent.wts(view_matrix) and ent.health > 0 and not ent.dormant:
                        color = Colors.cyan if ent.team != 2 else Colors.orange

                        head = ent.pos2d["y"] - ent.head_pos2d["y"]
                        width = head / 2
                        center = width / 2
                        if self.box_esp:
                            pm.draw_rectangle_lines(
                                ent.head_pos2d["x"] - center,
                                ent.head_pos2d["y"] - center / 2,
                                width,
                                head + center / 2,
                                color,
                                1.2,
                            )

                        health_color = Colors.green if ent.health > 50 else Colors.orange
                        draw_health_bar(ent, health_color, width, head)

                        if tracers:
                            pm.draw_line(
                                pm.get_screen_width() / 2,  # Start at the center of the screen
                                pm.get_screen_height(),     # Start from the bottom of the screen
                                ent.head_pos2d["x"],        # End at the head position X
                                ent.head_pos2d["y"],        # End at the head position Y
                                color,
                            )

                        circle_radius = (ent.pos2d["y"] - ent.head_pos2d["y"]) / 15
                        if self.head_esp:
                            pm.draw_circle_lines(
                                ent.head_pos2d["x"],
                                ent.head_pos2d["y"],
                                circle_radius,
                                color,
                            )

                        if self.skeleton_esp:
                            skeleton_positions = ent.skeleton(view_matrix)
                            for bones in Skeleton.bone_pairs:
                                if all(bone in skeleton_positions for bone in bones):
                                    for i in range(len(bones) - 1):
                                        start = bones[i]
                                        end = bones[i + 1]
                                        start_pos = skeleton_positions[start]
                                        end_pos = skeleton_positions[end]
                                        pm.draw_line(
                                            start_pos["x"],
                                            start_pos["y"],
                                            end_pos["x"],
                                            end_pos["y"],
                                            color,
                                            1.0,
                                        )

                pm.end_drawing()

            except Exception as e:
                print(f"[!] Error in ESP loop: {e}")
            time.sleep(0.01)  # Prevent CPU hogging
            
if __name__ == "__main__":
    print("Loading.. 🧪".center(columns))
    choices()