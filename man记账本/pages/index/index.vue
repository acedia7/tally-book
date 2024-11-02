<template>
	<view class="container">
		<view class="sa-head">
			<view class="content">
				<view class="ledger">
					<text>共{{sumCount}}笔 / 支{{sumExpend}}笔 / 收{{sumIncome}}笔 / 结余{{totalbalance}}</text>
				</view>
				<view class="line">
					<view class="item">
						<view class="text">{{nowTime.year}}年</view>
						<view class="content">
							<text>{{nowTime.month}}月</text>
							<text class="bar"></text>
						</view>
					</view>
					<view class="item">
						<view class="text">收入</view>
						<view class="content">{{totalIncome}}</view>
					</view>
					<view class="item">
						<view class="text">支出</view>
						<view class="content">{{totalExpend}}</view>
					</view>
				</view>
			</view>
		</view>
		<view class="sa-list">
			<view class="item" v-for="(item, index) in dataList" :key="index">
				<view class="count">
					<view class="sa-flex-x">
						<view>日期: {{item.create_time}}</view>
						<view class="week">({{item.create_time | weekFormat}})</view>
					</view>
				</view>
				<view class="sa-flex-x space content">
					<view class="sa-flex-x space">
						<view class="sa-flex-x center cover" :class="item.type==1 ? 'income':'expend'">
							<image :src="'../../static/icon/'+item.icon+'.png'" mode="aspectFill"></image>
						</view>
						<view class="info">
							<view class="name">{{item.content}}</view>
							<view class="desc" v-if="item.remarks">{{item.remarks}}</view>
						</view>
					</view>
					<view class="sa-flex-x money" :class="item.type==1 ? 'income':'expend'">
						<text class="symbol">{{item.type==1 ? '+':'-'}}</text>
						<text>{{item.money}}</text>
					</view>
				</view>
			</view>
		</view>
		<view class="sa-flex-y center sa-error" v-if="dataList.length == 0">
			<view class="info">
				<image class="cover" src="@/static/nocon.png" mode="aspectFit"></image>
				<view class="text">~ 美好生活，米粒相伴 ~</view>
			</view>
		</view>
	</view>
</template>
<script>
	import format from '@/utils/format';
	export default {
		data() {
			return {
				sumCount: 0,
				sumExpend: 0,
				sumIncome: 0,
				totalExpend: 0,
				totalIncome: 0,
				totalbalance: 0,
				dataList: [],
				nowTime: {
					all: '',
					year: '0000',
					month: '00',
					day: '00'
				}
			}
		},
		onLoad() {
			const str = format.getSysDate();
			const date = str.split('-');
			this.nowTime = {all: str,year: date[0],month: date[1],day: date[2]}
		},
		onShow() {
			this.getData();
		},
		filters: {
			weekFormat(val) {
				return format.getWeekDay(val);
			}
		},
		methods: {
			getData() {
				uni.getStorage({
					key: 'sa_storage_bill',
					success: res => {
						const data = JSON.parse(res.data);
						this.dataList = JSON.parse(res.data);
						this.total();
					}
				})
			},
			total() {
				const data = this.dataList;
				const group = format.arrayGroup(data, 'type');
				if(Object.keys(group).length > 0) {
					const expendMoney = group[0].reduce((sum, item) => sum + Number(item.money), 0);
					this.totalExpend = expendMoney.toFixed(2);
					this.sumExpend = group[0].length;
				}
				if(Object.keys(group).length > 1) {
					const incomeMoney = group[1].reduce((sum, item) => sum + Number(item.money), 0);
					this.totalIncome = incomeMoney.toFixed(2);
					this.sumIncome = group[1].length;
				}
				this.sumCount = data.length;
				this.totalbalance = (this.totalIncome - this.totalExpend).toFixed(2); 
			}
		}
	}
</script>
<style lang="less">
	.sa-head {
		top: 0;
		left: 0;
		right: 0;
		z-index: 1;
		background-color: #07c160;
		padding: 0 30rpx;
		.content {
			height: 230rpx;
			.ledger {
				padding-bottom: 20rpx;
				border-bottom: 2rpx solid rgba(255,255,255,0.1);
				text {
					font-size: 32rpx;
					color: #fff;
				}
			}
			.line {
				display: flex;
				color: #fff;
				padding-top: 30rpx;
				.item {
					flex: 1;
					.text {
						font-size: 28rpx;
					}
					.meter {
						width: 120rpx;
					}
					.content {
						height: 50rpx;
						line-height: 50rpx;
						margin-top: 20rpx;
						font-size: 40rpx;
						.month {
							top: 0;
							left: 46rpx;
							font-size: 36rpx;
						}
						.sa {
							font-size: 36rpx;
						}
						.bar {
							padding-left: 50rpx;
							border-right-width: 1px;
							border-right-style: solid;
							height: 40rpx;
							transform: scaleX(0.5);
							border-color: rgba(255,255,255,0.3);
						}
					}
				}
			}
		}
	}
	.sa-list {
		margin-top: 20rpx;
		.item {
			background-color: #fff;
			margin: 0 20rpx 20rpx 20rpx;
			padding: 30rpx 0 10rpx 0;
			border-radius: 20rpx;
			.count {
				margin: 0 30rpx;
				padding-bottom: 20rpx;
				font-size: 28rpx;
				border-bottom: 1px solid #f5f5f5;
				.week {
					margin-left: 10rpx;
				}
			}
			.content {
				margin: 0 30rpx;
				padding: 20rpx 0;
			}
			.cover {
				width: 80rpx;
				height: 80rpx;
				border-radius: 50%;
				&.expend {
					background-color: #07c160;
				}
				&.income {
					background-color: #f1b73a;
				}
				image {
					width: 40rpx;
					height: 40rpx;
				}
			}
			.info {
				width: 360rpx;
				margin-left: 30rpx;
				width: 300rpx;
				.name {
					font-size: 32rpx;
					color: #000;
				}
				.desc {
					font-size: 28rpx;
					color: #999;
				}
			}
			.money {
				&.expend {
					color: #000;
				}
				&.income {
					color: #f1b73a;
				}
				.symbol {
					margin-right: 5rpx;
					font-weight: bold;
				}
			}
			&:last-child{
				margin-bottom: 0;
			}
		}
	}
	.sa-error {
		height: 100%;
		text-align: center;
		.info {
			width: 400rpx;
			padding-top: 300rpx;
			.cover {
				height: 180rpx;
				width: 100%;
				margin-bottom: 20rpx;
			}
			.text {
				color: #a7a7a7;
				font-size: 32rpx;
			}
		}
	}
</style>