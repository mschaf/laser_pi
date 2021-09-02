class DashboardController < ApplicationController


  def show
    @devices = Device.all
    if request.headers['X-Up-Target'].include? '.poller'
      render 'status'
    end
  end


end