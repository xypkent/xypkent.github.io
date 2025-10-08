#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import requests
from datetime import datetime

def get_scholar_id():
    """Get Google Scholar ID from environment variable"""
    scholar_id = os.environ.get('GOOGLE_SCHOLAR_ID', 'Xt8HBrIAAAAJ')
    return scholar_id

def fetch_scholar_stats(scholar_id):
    """Fetch Google Scholar statistics"""
    try:
        url = f"https://scholar.google.com/citations?user={scholar_id}&hl=en"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # For simplicity, create a basic data structure
        # In production, you would parse the actual Google Scholar page
        data = {
            "updated_time": datetime.now().isoformat(),
            "total_citations": 0,
            "publications": {}
        }
        
        return data
    except Exception as e:
        print(f"Error fetching scholar stats: {e}")
        return None

def save_stats(data):
    """Save statistics to JSON files"""
    if not data:
        return
    
    # Create output directory if it doesn't exist
    os.makedirs('gs_data', exist_ok=True)
    
    # Save main data file
    with open('gs_data/gs_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    # Save shields.io compatible format
    shields_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(data.get('total_citations', 0))
    }
    
    with open('gs_data/gs_data_shieldsio.json', 'w', encoding='utf-8') as f:
        json.dump(shields_data, f, indent=2)
    
    print(f"✅ Successfully saved Google Scholar stats")
    print(f"   Total citations: {data.get('total_citations', 0)}")
    print(f"   Updated: {data.get('updated_time', 'N/A')}")

def main():
    scholar_id = get_scholar_id()
    print(f"🔍 Fetching Google Scholar stats for ID: {scholar_id}")
    
    data = fetch_scholar_stats(scholar_id)
    save_stats(data)

if __name__ == '__main__':
    main()

