SELECT el.id, el.emotion_id, e.name, el.confidence, el.created_at FROM emotion_log el JOIN emotion e ON el.emotion_id = e.id ORDER BY el.created_at;