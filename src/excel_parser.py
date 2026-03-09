def parse_excel(file_path):
    # Improved machine detection
    # ...
    for row in data:
        if 'ash ac' in row[19] or 'ahp' in row[19]:  # Updated line 19
            # Process for ash ac or ahp
            pass
        if 'rated' in row[36]:  # Added 'and rated' check
            # Detect rated_fad
            pass
        # ...

        if 'sec' in row[45]:  # Updated line 45
            # Process for SEC
            pass
