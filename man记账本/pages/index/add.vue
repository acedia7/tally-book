<template>
	<view class="container">
		<view class="sa-flex-x center sa-tabs">
			<button class="item" hover-class="" v-for="(item, index) in tabList" :key="index" @tap="index!=tabId ? onTab(0, index):''">
				<view class="title" :class="{'active':index == tabId}">{{item}}</view>
			</button>
		</view>
		<view class="sa-category">
			<button class="item" hover-class="" v-for="(item, index) in classList" :key="index" @tap="onTab(1, index)">
				<view class="sa-flex-x center icon" :class="{'active':index+1 == subId}">
					<image :src="'../../static/icon/'+item.icon+'.png'" mode="aspectFill"></image>
				</view>
				<view class="name" :class="{'active':index+1 == subId}">{{item.title.slice(0, 4)}}</view>
			</button>
		</view>
		<view class="sa-value">
			<input type="digit" v-model="keyVal" placeholder-class="placeholder" placeholder="输入金额" />
		</view>
		<view class="sa-value mt20">
			<input v-model="textRemarks" placeholder-class="placeholder" placeholder="账单备注" />
		</view>
		<button class="sa-save" hover-class="" @click="btnForm">保存</button>
	</view>
</template>
<script>
	import format from '@/utils/format';
	export default {
		data() {
			return {
				tabId: 0,
				subId: 0,
				classList: [],
				keyVal: '',
				textRemarks: '',
				tabList: ['支出','收入'],
				expend: [
					{
						id: 1,
						title: '餐饮',
						icon: 'canyin'
					},
					{
						id: 2,
						title: '交通',
						icon: 'jiaotong'
					},
					{
						id: 3,
						title: '娱乐',
						icon: 'yule'
					},
					{
						id: 4,
						title: '日用',
						icon: 'riyong'
					},
					{
						id: 5,
						title: '住房',
						icon: 'zhufang'
					},
					{
						id: 6,
						title: '水电',
						icon: 'shuidian'
					},
					{
						id: 7,
						title: '医疗',
						icon: 'yiliao'
					},
					{
						id: 8,
						title: '其它',
						icon: 'qita'
					}
				],
				income: [
					{
						id: 1,
						title: '工资',
						icon: 'gongzi'
					},
					{
						id: 2,
						title: '奖金',
						icon: 'jiangjin'
					},
					{
						id: 3,
						title: '兼职',
						icon: 'jianzhi'
					}
				]
			}
		},
		onShow() {
			this.tabId = 0;
			this.subId = 0;
			this.keyVal = '';
			this.textRemarks = '';
			this.classList = this.expend;
		},
		methods: {
			onTab(type, index) {
				if(type == 1) {
					this.subId = index + 1;
				}else{
					this.subId = 0;
					this.tabId = index;
					this.keyVal = '';
					if(index == 1) {
						this.classList = this.income;
					}else{
						this.classList = this.expend;
					}
				}
			},
			async btnForm() {
				try {
					if(this.subId == 0) {
					  throw '请选择记录类别';
					}
					if(this.keyVal == '' || this.keyVal == 0) {
					  throw '请输入记录金额';
					}
				}catch (err) {
					uni.showToast({title: err,icon: 'none',duration: 1000});
				  return false;
				}
				this.save();
			},
			save() {
				const parm = {
					type: this.tabId,
					icon: this.classList[this.subId-1].icon,
					content: this.classList[this.subId-1].title,
					money: this.keyVal,
					remarks: this.textRemarks,
					create_time: format.getSysDate()
				};
				uni.getStorage({
					key: 'sa_storage_bill',
					success: (res) => {
						let classData = JSON.parse(res.data);
						classData.push(parm);
						uni.setStorage({key: 'sa_storage_bill', data: JSON.stringify(classData.reverse())});
					},
					fail: (err) => {
						uni.setStorage({
							key: 'sa_storage_bill',
							data: JSON.stringify([parm])
						})
					}
				})
				uni.switchTab({url: `/pages/index/index`});
			}
		}
	}
</script>
<style lang="less">
	.sa-tabs {
		min-height: 40px;
		margin: 0 20rpx;
		background-color: #bee2f5;
		border-bottom: 1px solid #f5f5f5;
		border-radius: 20rpx 20rpx 0 0;
		.item {
			padding: 0 20rpx;
			.title {
				font-size: 32rpx;
				color: #000;
				&.active {
					font-size: 36rpx;
					font-weight: bold;
				}
			}
		}
	}
	.sa-category {
		box-sizing: border-box;
		display: flex;
		flex-wrap: wrap;
		background-color: #fff;
		padding: 20rpx 0;
		margin: 0 20rpx 30rpx 20rpx;
		border-radius: 0 0 20rpx 20rpx;
		.item {
			display: flex;
			flex-direction: column;
			align-items: center;
			width: 20%;
			padding: 10rpx 0;
			.icon {
				width: 100rpx;
				height: 100rpx;
				font-size: 48rpx;
				border-radius: 50%;
				color: #fff;
				background-color: #f3f3f3;
				&.active {
					background-color: #bee2f5;
				}
				image {
					width: 50rpx;
					height: 50rpx;
				}
				&.active {
					background-color: #bee2f5;
					color: #fff;
				}
				&.add {
					width: 96rpx;
					height: 96rpx;
					border: 2rpx dashed #999;
				}
			}
			.name {
				margin-top: 10rpx;
				font-size: 30rpx;
				color: #000;
				&.active {
					color: #0e4f71;
				}
			}
		}
	}
	.sa-value {
		background-color: #fff;
		height: 80rpx;
		margin: 0 20rpx;
		padding: 20rpx 40rpx;
		border-radius: 20rpx;
		&.mt20 {
			margin-top: 30rpx;
		}
		input {
			height: 80rpx;
			width: 100%;
			font-size: 32rpx;
			&.placeholder {
				font-size: 32rpx;
			}
		}
	}
	.sa-save {
		margin: 30rpx 20rpx;
		height: 120rpx;
		line-height: 120rpx;
		font-size: 36rpx;
		text-align: center;
		background-color: #0e4f71;
		color: #fff;
		border-radius: 20rpx;
	}
</style>
