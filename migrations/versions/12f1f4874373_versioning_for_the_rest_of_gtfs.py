"""versioning for the rest of gtfs

Revision ID: 12f1f4874373
Revises: 3f5919056083
Create Date: 2015-10-27 14:44:30.712020

"""

# revision identifiers, used by Alembic.
revision = '12f1f4874373'
down_revision = '3f5919056083'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agency_version',
                    sa.Column('agency_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('agency_name', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('agency_url', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('agency_timezone', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('agency_lang', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('agency_phone', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('agency_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_agency_version_end_transaction_id'), 'agency_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_agency_version_operation_type'), 'agency_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_agency_version_transaction_id'), 'agency_version', ['transaction_id'], unique=False)
    op.create_table('calendar_dates_version',
                    sa.Column('service_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('date', sa.String(length=50), autoincrement=False, nullable=False),
                    sa.Column('exception_type', sa.String(length=50), autoincrement=False, nullable=False),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('service_id', 'date', 'exception_type', 'transaction_id')
                    )
    op.create_index(op.f('ix_calendar_dates_version_end_transaction_id'), 'calendar_dates_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_calendar_dates_version_operation_type'), 'calendar_dates_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_calendar_dates_version_transaction_id'), 'calendar_dates_version', ['transaction_id'], unique=False)
    op.create_table('calendar_version',
                    sa.Column('service_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('service_name', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('start_date', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('end_date', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('monday', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('tuesday', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('wednesday', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('thursday', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('friday', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('saturday', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('sunday', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('service_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_calendar_version_end_transaction_id'), 'calendar_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_calendar_version_operation_type'), 'calendar_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_calendar_version_transaction_id'), 'calendar_version', ['transaction_id'], unique=False)
    op.create_table('fare_attributes_version',
                    sa.Column('fare_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('price', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('currency_type', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('payment_method', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transfers', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transfer_duration', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('fare_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_fare_attributes_version_end_transaction_id'), 'fare_attributes_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_fare_attributes_version_operation_type'), 'fare_attributes_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_fare_attributes_version_transaction_id'), 'fare_attributes_version', ['transaction_id'], unique=False)
    op.create_table('fare_rules_version',
                    sa.Column('fare_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('route_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('origin_id', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('destination_id', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('contains_id', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('fare_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_fare_rules_version_end_transaction_id'), 'fare_rules_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_fare_rules_version_operation_type'), 'fare_rules_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_fare_rules_version_transaction_id'), 'fare_rules_version', ['transaction_id'], unique=False)
    op.create_table('feed_info_version',
                    sa.Column('feed_publisher_name', sa.String(length=50), autoincrement=False, nullable=False),
                    sa.Column('feed_publisher_url', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('feed_lang', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('feed_version', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('feed_start_date', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('feed_end_date', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('feed_publisher_name', 'transaction_id')
                    )
    op.create_index(op.f('ix_feed_info_version_end_transaction_id'), 'feed_info_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_feed_info_version_operation_type'), 'feed_info_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_feed_info_version_transaction_id'), 'feed_info_version', ['transaction_id'], unique=False)
    op.create_table('frequencies_version',
                    sa.Column('trip_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('start_time', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('end_time', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('headway_secs', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('exact_times', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('trip_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_frequencies_version_end_transaction_id'), 'frequencies_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_frequencies_version_operation_type'), 'frequencies_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_frequencies_version_transaction_id'), 'frequencies_version', ['transaction_id'], unique=False)
    op.create_table('route_frequencies_version',
                    sa.Column('route_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('service_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('start_time', sa.String(length=50), autoincrement=False, nullable=False),
                    sa.Column('end_time', sa.String(length=50), autoincrement=False, nullable=False),
                    sa.Column('headway_secs', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('route_id', 'service_id', 'start_time', 'end_time', 'transaction_id')
                    )
    op.create_index(op.f('ix_route_frequencies_version_end_transaction_id'), 'route_frequencies_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_route_frequencies_version_operation_type'), 'route_frequencies_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_route_frequencies_version_transaction_id'), 'route_frequencies_version', ['transaction_id'], unique=False)
    op.create_table('shape_paths_version',
                    sa.Column('shape_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('shape_path', sa.UnicodeText(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('shape_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_shape_paths_version_end_transaction_id'), 'shape_paths_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_shape_paths_version_operation_type'), 'shape_paths_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_shape_paths_version_transaction_id'), 'shape_paths_version', ['transaction_id'], unique=False)
    op.create_table('shapes_version',
                    sa.Column('shape_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('shape_pt_lat', sa.Float(precision=53), autoincrement=False, nullable=True),
                    sa.Column('shape_pt_lon', sa.Float(precision=53), autoincrement=False, nullable=True),
                    sa.Column('shape_pt_time', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('shape_pt_sequence', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('shape_id', 'shape_pt_sequence', 'transaction_id')
                    )
    op.create_index(op.f('ix_shapes_version_end_transaction_id'), 'shapes_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_shapes_version_operation_type'), 'shapes_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_shapes_version_transaction_id'), 'shapes_version', ['transaction_id'], unique=False)
    op.create_table('stop_seq_version',
                    sa.Column('trip_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('stop_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('stop_sequence', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('stop_time', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('shape_dist_traveled', sa.Float(precision=53), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('trip_id', 'stop_id', 'stop_sequence', 'transaction_id')
                    )
    op.create_index(op.f('ix_stop_seq_version_end_transaction_id'), 'stop_seq_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_stop_seq_version_operation_type'), 'stop_seq_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_stop_seq_version_transaction_id'), 'stop_seq_version', ['transaction_id'], unique=False)
    op.create_table('stop_times_version',
                    sa.Column('trip_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('stop_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('stop_sequence', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('arrival_time', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('departure_time', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('shape_dist_traveled', sa.Float(precision=53), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('trip_id', 'stop_id', 'stop_sequence', 'transaction_id')
                    )
    op.create_index(op.f('ix_stop_times_version_end_transaction_id'), 'stop_times_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_stop_times_version_operation_type'), 'stop_times_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_stop_times_version_transaction_id'), 'stop_times_version', ['transaction_id'], unique=False)
    op.create_table('stops_version',
                    sa.Column('stop_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('stop_code', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('stop_desc', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('stop_name', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('stop_lat', sa.Float(precision=53), autoincrement=False, nullable=True),
                    sa.Column('stop_lon', sa.Float(precision=53), autoincrement=False, nullable=True),
                    sa.Column('stop_calle', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('stop_numero', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('stop_entre', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('stop_esquina', sa.String(length=250), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('stop_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_stops_version_end_transaction_id'), 'stops_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_stops_version_operation_type'), 'stops_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_stops_version_transaction_id'), 'stops_version', ['transaction_id'], unique=False)
    op.create_table('transfers_version',
                    sa.Column('from_stop_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('to_stop_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('transfer_type', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('from_stop_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_transfers_version_end_transaction_id'), 'transfers_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_transfers_version_operation_type'), 'transfers_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_transfers_version_transaction_id'), 'transfers_version', ['transaction_id'], unique=False)
    op.create_table('trips_start_times_version',
                    sa.Column('trip_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('service_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('start_time', sa.String(length=50), autoincrement=False, nullable=False),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('trip_id', 'service_id', 'start_time', 'transaction_id')
                    )
    op.create_index(op.f('ix_trips_start_times_version_end_transaction_id'), 'trips_start_times_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_trips_start_times_version_operation_type'), 'trips_start_times_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_trips_start_times_version_transaction_id'), 'trips_start_times_version', ['transaction_id'], unique=False)
    op.create_table('trips_version',
                    sa.Column('trip_id', sa.Integer(), autoincrement=False, nullable=False),
                    sa.Column('route_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('service_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('trip_headsign', sa.String(length=150), autoincrement=False, nullable=True),
                    sa.Column('trip_short_name', sa.String(length=150), autoincrement=False, nullable=True),
                    sa.Column('direction_id', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('shape_id', sa.Integer(), autoincrement=False, nullable=True),
                    sa.Column('card_code', sa.String(length=50), autoincrement=False, nullable=True),
                    sa.Column('active', sa.Boolean(), autoincrement=False, nullable=True),
                    sa.Column('transaction_id', sa.BigInteger(), autoincrement=False, nullable=False),
                    sa.Column('end_transaction_id', sa.BigInteger(), nullable=True),
                    sa.Column('operation_type', sa.SmallInteger(), nullable=False),
                    sa.PrimaryKeyConstraint('trip_id', 'transaction_id')
                    )
    op.create_index(op.f('ix_trips_version_end_transaction_id'), 'trips_version', ['end_transaction_id'], unique=False)
    op.create_index(op.f('ix_trips_version_operation_type'), 'trips_version', ['operation_type'], unique=False)
    op.create_index(op.f('ix_trips_version_transaction_id'), 'trips_version', ['transaction_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_trips_version_transaction_id'), table_name='trips_version')
    op.drop_index(op.f('ix_trips_version_operation_type'), table_name='trips_version')
    op.drop_index(op.f('ix_trips_version_end_transaction_id'), table_name='trips_version')
    op.drop_table('trips_version')
    op.drop_index(op.f('ix_trips_start_times_version_transaction_id'), table_name='trips_start_times_version')
    op.drop_index(op.f('ix_trips_start_times_version_operation_type'), table_name='trips_start_times_version')
    op.drop_index(op.f('ix_trips_start_times_version_end_transaction_id'), table_name='trips_start_times_version')
    op.drop_table('trips_start_times_version')
    op.drop_index(op.f('ix_transfers_version_transaction_id'), table_name='transfers_version')
    op.drop_index(op.f('ix_transfers_version_operation_type'), table_name='transfers_version')
    op.drop_index(op.f('ix_transfers_version_end_transaction_id'), table_name='transfers_version')
    op.drop_table('transfers_version')
    op.drop_index(op.f('ix_stops_version_transaction_id'), table_name='stops_version')
    op.drop_index(op.f('ix_stops_version_operation_type'), table_name='stops_version')
    op.drop_index(op.f('ix_stops_version_end_transaction_id'), table_name='stops_version')
    op.drop_table('stops_version')
    op.drop_index(op.f('ix_stop_times_version_transaction_id'), table_name='stop_times_version')
    op.drop_index(op.f('ix_stop_times_version_operation_type'), table_name='stop_times_version')
    op.drop_index(op.f('ix_stop_times_version_end_transaction_id'), table_name='stop_times_version')
    op.drop_table('stop_times_version')
    op.drop_index(op.f('ix_stop_seq_version_transaction_id'), table_name='stop_seq_version')
    op.drop_index(op.f('ix_stop_seq_version_operation_type'), table_name='stop_seq_version')
    op.drop_index(op.f('ix_stop_seq_version_end_transaction_id'), table_name='stop_seq_version')
    op.drop_table('stop_seq_version')
    op.drop_index(op.f('ix_shapes_version_transaction_id'), table_name='shapes_version')
    op.drop_index(op.f('ix_shapes_version_operation_type'), table_name='shapes_version')
    op.drop_index(op.f('ix_shapes_version_end_transaction_id'), table_name='shapes_version')
    op.drop_table('shapes_version')
    op.drop_index(op.f('ix_shape_paths_version_transaction_id'), table_name='shape_paths_version')
    op.drop_index(op.f('ix_shape_paths_version_operation_type'), table_name='shape_paths_version')
    op.drop_index(op.f('ix_shape_paths_version_end_transaction_id'), table_name='shape_paths_version')
    op.drop_table('shape_paths_version')
    op.drop_index(op.f('ix_route_frequencies_version_transaction_id'), table_name='route_frequencies_version')
    op.drop_index(op.f('ix_route_frequencies_version_operation_type'), table_name='route_frequencies_version')
    op.drop_index(op.f('ix_route_frequencies_version_end_transaction_id'), table_name='route_frequencies_version')
    op.drop_table('route_frequencies_version')
    op.drop_index(op.f('ix_frequencies_version_transaction_id'), table_name='frequencies_version')
    op.drop_index(op.f('ix_frequencies_version_operation_type'), table_name='frequencies_version')
    op.drop_index(op.f('ix_frequencies_version_end_transaction_id'), table_name='frequencies_version')
    op.drop_table('frequencies_version')
    op.drop_index(op.f('ix_feed_info_version_transaction_id'), table_name='feed_info_version')
    op.drop_index(op.f('ix_feed_info_version_operation_type'), table_name='feed_info_version')
    op.drop_index(op.f('ix_feed_info_version_end_transaction_id'), table_name='feed_info_version')
    op.drop_table('feed_info_version')
    op.drop_index(op.f('ix_fare_rules_version_transaction_id'), table_name='fare_rules_version')
    op.drop_index(op.f('ix_fare_rules_version_operation_type'), table_name='fare_rules_version')
    op.drop_index(op.f('ix_fare_rules_version_end_transaction_id'), table_name='fare_rules_version')
    op.drop_table('fare_rules_version')
    op.drop_index(op.f('ix_fare_attributes_version_transaction_id'), table_name='fare_attributes_version')
    op.drop_index(op.f('ix_fare_attributes_version_operation_type'), table_name='fare_attributes_version')
    op.drop_index(op.f('ix_fare_attributes_version_end_transaction_id'), table_name='fare_attributes_version')
    op.drop_table('fare_attributes_version')
    op.drop_index(op.f('ix_calendar_version_transaction_id'), table_name='calendar_version')
    op.drop_index(op.f('ix_calendar_version_operation_type'), table_name='calendar_version')
    op.drop_index(op.f('ix_calendar_version_end_transaction_id'), table_name='calendar_version')
    op.drop_table('calendar_version')
    op.drop_index(op.f('ix_calendar_dates_version_transaction_id'), table_name='calendar_dates_version')
    op.drop_index(op.f('ix_calendar_dates_version_operation_type'), table_name='calendar_dates_version')
    op.drop_index(op.f('ix_calendar_dates_version_end_transaction_id'), table_name='calendar_dates_version')
    op.drop_table('calendar_dates_version')
    op.drop_index(op.f('ix_agency_version_transaction_id'), table_name='agency_version')
    op.drop_index(op.f('ix_agency_version_operation_type'), table_name='agency_version')
    op.drop_index(op.f('ix_agency_version_end_transaction_id'), table_name='agency_version')
    op.drop_table('agency_version')
    ### end Alembic commands ###
