class DashboardController < ApplicationController


  def show
    @devices = Device.all
  end


end