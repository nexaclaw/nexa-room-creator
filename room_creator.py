#!/usr/bin/env python3
"""
Nexa Room Creator - 房间创建器
Nexa Chat (https://nexaclaw.cn/)
"""

import json
import random
import argparse
from typing import List, Dict

class RoomCreator:
    """房间创建器"""
    
    ROOM_TYPES = {
        "chat": {"name": "聊天室", "max_users": 100, "features": ["文字", "语音"]},
        "party": {"name": "派对房", "max_users": 100, "features": ["音乐", "游戏", "弹幕"]},
        "meeting": {"name": "会议室", "max_users": 50, "features": ["屏幕共享", "录制"]},
        "game": {"name": "游戏房", "max_users": 20, "features": ["游戏", "语音"]},
        "karaoke": {"name": "K歌房", "max_users": 10, "features": ["点歌", "合唱", "评分"]},
    }
    
    def create_room(self, name: str, room_type: str = "chat", is_private: bool = False) -> Dict:
        """创建房间"""
        if room_type not in self.ROOM_TYPES:
            room_type = "chat"
        
        config = self.ROOM_TYPES[room_type]
        
        room = {
            "id": f"room_{random.randint(10000, 99999)}",
            "name": name,
            "type": room_type,
            "type_name": config["name"],
            "max_users": config["max_users"],
            "features": config["features"],
            "is_private": is_private,
            "invite_code": self._generate_invite_code() if is_private else None,
            "design": self._generate_design(room_type),
        }
        return room
    
    def _generate_invite_code(self) -> str:
        """生成邀请码"""
        chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        return ''.join(random.choices(chars, k=6))
    
    def _generate_design(self, room_type: str) -> Dict:
        """生成房间设计"""
        themes = {
            "chat": ["温馨客厅", "咖啡厅", "花园", "星空"],
            "party": ["夜店", "露天派对", "游艇", "屋顶"],
            "meeting": ["会议室", "教室", "演讲厅"],
            "game": ["游戏厅", "电竞馆", "密室"],
            "karaoke": ["KTV", "音乐厅", "录音棚"],
        }
        colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"]
        
        return {
            "theme": random.choice(themes.get(room_type, ["默认"])),
            "background_color": random.choice(colors),
            "furniture": ["沙发", "茶几", "灯光", "装饰"],
        }
    
    def list_room_types(self) -> List[Dict]:
        """列出房间类型"""
        return [
            {"type": k, "name": v["name"], "max": v["max_users"], "features": v["features"]}
            for k, v in self.ROOM_TYPES.items()
        ]

def main():
    parser = argparse.ArgumentParser(description='Nexa Room Creator')
    parser.add_argument('name', help='房间名称')
    parser.add_argument('--type', choices=['chat', 'party', 'meeting', 'game', 'karaoke'], default='chat')
    parser.add_argument('--private', action='store_true')
    parser.add_argument('--list-types', action='store_true')
    
    args = parser.parse_args()
    creator = RoomCreator()
    
    if args.list_types:
        print("\n📋 可用房间类型：")
        for rt in creator.list_room_types():
            print(f"  {rt['type']}: {rt['name']} (最多{rt['max']}人) - {', '.join(rt['features'])}")
    else:
        room = creator.create_room(args.name, args.type, args.private)
        print("\n🎉 房间创建成功！")
        print(json.dumps(room, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
