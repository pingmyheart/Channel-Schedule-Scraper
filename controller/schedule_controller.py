from flask import Blueprint, jsonify, request

from configuration.logging_configuration import logger as log
from service import schedule_service_bean

schedule_bp = Blueprint('schedule', __name__, url_prefix='/channel-schedule-scraper/schedule')


@schedule_bp.route('/channels', methods=['GET'])
def get_all_channels():
    log.info("[INCOMING REQUEST] - Get All Channels")
    service_response = schedule_service_bean.get_available_channels()
    return jsonify(service_response.dict(exclude_none=True)), 200


@schedule_bp.route('', methods=['GET'])
def get_channel_schedule():
    log.info("[INCOMING REQUEST] - Get Channel Schedule")
    channel_href = request.args.get('channel_href')
    if not channel_href:
        return jsonify({"error": "Channel ID is required"}), 400
    service_response = schedule_service_bean.get_schedule_by_channel(channel_href=channel_href)
    return jsonify(service_response.dict(exclude_none=True)), 200
