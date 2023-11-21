import mediapipe as mp
from math import degrees, acos
import numpy as np


mp_hands = mp.solutions.hands


def obtenerAngulos(results, width, height):

    def get_xy(index):
        return [
            int(hand_landmarks.landmark[index].x * width),
            int(hand_landmarks.landmark[index].y * height),
        ]

    for hand_landmarks in results.multi_hand_landmarks:
        # Diccionario de coordenadas de cada dedo
        dedos = {
            "meñique": [
                get_xy(mp_hands.HandLandmark.PINKY_TIP),
                get_xy(mp_hands.HandLandmark.PINKY_PIP),
                get_xy(mp_hands.HandLandmark.PINKY_MCP),
            ],
            "anular": [
                get_xy(mp_hands.HandLandmark.RING_FINGER_TIP),
                get_xy(mp_hands.HandLandmark.RING_FINGER_PIP),
                get_xy(mp_hands.HandLandmark.RING_FINGER_MCP),
            ],
            "medio": [
                get_xy(mp_hands.HandLandmark.MIDDLE_FINGER_TIP),
                get_xy(mp_hands.HandLandmark.MIDDLE_FINGER_PIP),
                get_xy(mp_hands.HandLandmark.MIDDLE_FINGER_MCP),
            ],
            "indice": [
                get_xy(mp_hands.HandLandmark.INDEX_FINGER_TIP),
                get_xy(mp_hands.HandLandmark.INDEX_FINGER_PIP),
                get_xy(mp_hands.HandLandmark.INDEX_FINGER_MCP),
            ],
            "pulgar": [
                get_xy(mp_hands.HandLandmark.THUMB_TIP),
                get_xy(mp_hands.HandLandmark.THUMB_IP),
                get_xy(mp_hands.HandLandmark.THUMB_MCP),
            ],
            "pulgar_interno": [
                get_xy(mp_hands.HandLandmark.THUMB_TIP),
                get_xy(mp_hands.HandLandmark.THUMB_MCP),
                get_xy(mp_hands.HandLandmark.WRIST),
            ],
        }
        
        dedos_array = np.concatenate([np.array(dedo) for dedo in dedos.values()])
        
        puntos = dedos_array.reshape(-1, 3, 2)
    
        l_list = np.linalg.norm(puntos[:, [0, 1], :] - puntos[:, [1, 2], :], axis=2)

        num_den_list = np.sum(
            (puntos[:, 0, :] - puntos[:, 1, :]) * (puntos[:, 2, :] - puntos[:, 1, :]),
            axis=1,
        ) / (l_list[:, 0] * l_list[:, 1])

        angulos = np.degrees(np.arccos(num_den_list))
        pinky = [
            int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * width),
            int(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * height),
        ]
        angulos = angulos.tolist()
        return [angulos, pinky]